seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = 'AUG'
stop_codons = {'UAA', 'UAG', 'UGA'}

longest_orf = ''

for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        for j in range(i + 3, len(seq) - 2, 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf = seq[i:j+3]   # 包含 stop codon
                if len(orf) > len(longest_orf):
                    longest_orf = orf
                break

if longest_orf:
    print("Longest ORF:", longest_orf)
    print("Length:", len(longest_orf))
else:
    print("No ORF found")