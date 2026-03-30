import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output_file = os.path.join(script_dir, 'stop_genes.fa')

start_codon = 'ATG'
stop_codons = {'TAA', 'TAG', 'TGA'}

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
                header = line[1:]   # 去掉 >
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


def find_stop_codons_in_orfs(seq):
    found = set()

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found.add(codon)
                    break

    return sorted(found)


with open(output_file, 'w') as out:
    count = 0

    for header, seq in read_fasta(fasta_file):
        gene_name = get_gene_name(header)
        found_stops = find_stop_codons_in_orfs(seq)

        if found_stops:
            out.write(f">{gene_name} {','.join(found_stops)}\n")
            out.write(seq + "\n")
            count += 1

print(f"Done. Wrote {count} genes to {output_file}")