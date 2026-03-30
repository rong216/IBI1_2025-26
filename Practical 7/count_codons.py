import re
import os
from collections import Counter
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

all_stop_codons = {'TAA', 'TAG', 'TGA'}
start_codon = 'ATG'


def read_fasta(filename):
    header = None
    seq_parts = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith('>'):
                if header is not None:
                    yield header, ''.join(seq_parts).upper()
                header = line[1:]
                seq_parts = []
            else:
                seq_parts.append(line)

        if header is not None:
            yield header, ''.join(seq_parts).upper()


def get_gene_name(header):
    match = re.search(r'gene:([^\s]+)', header)
    if match:
        return match.group(1)
    return header.split()[0]


def longest_orf_for_stop(seq, wanted_stop):
    best_orf = None

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]

                if codon in all_stop_codons:
                    if codon == wanted_stop:
                        orf = seq[i:j+3]
                        if best_orf is None or len(orf) > len(best_orf):
                            best_orf = orf
                    break

    return best_orf


wanted_stop = input("Enter stop codon (TAA, TAG, TGA): ").strip().upper()

if wanted_stop not in all_stop_codons:
    print("Invalid input. Please enter TAA, TAG, or TGA.")
    raise SystemExit

codon_counts = Counter()
genes_used = 0

for header, seq in read_fasta(fasta_file):
    gene_name = get_gene_name(header)
    best_orf = longest_orf_for_stop(seq, wanted_stop)

    if best_orf:
        genes_used += 1

        upstream = best_orf[:-3]  # 去掉最后的 stop codon
        for i in range(0, len(upstream), 3):
            codon = upstream[i:i+3]
            if len(codon) == 3:
                codon_counts[codon] += 1

print(f"Genes containing in-frame {wanted_stop}: {genes_used}")
print("Codon counts upstream of the chosen stop codon:")

for codon, count in sorted(codon_counts.items()):
    print(codon, count)

# 画 pie chart 并保存
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

if sizes:
    fig, ax = plt.subplots(figsize=(10, 10))
    wedges, texts, autotexts = ax.pie(
        sizes,
        autopct='%1.1f%%',
        startangle=90
    )
    ax.set_title(f'In-frame codon distribution upstream of {wanted_stop}')
    ax.legend(
        wedges,
        labels,
        title="Codons",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )
    plt.tight_layout()
    output_plot = f'codon_pie_{wanted_stop}.png'
    plt.savefig(output_plot, dpi=300)
    plt.close()

    print(f"Pie chart saved to {output_plot}")
else:
    print("No ORFs found for that stop codon.")