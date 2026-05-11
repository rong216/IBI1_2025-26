from pathlib import Path

def read_fasta(filename):
    """
    Read a FASTA-like file and return the sequence.
    This also works if the file only contains the raw sequence.
    """
    text = Path(filename).read_text().strip()
    lines = text.splitlines()

    sequence_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            continue
        sequence_lines.append(line)

    return "".join(sequence_lines)


def calculate_identity(seq1, seq2):
    """
    Calculate percentage identity for two sequences of the same length.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length for non-gapped alignment.")

    identical = 0

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            identical += 1

    percentage_identity = identical / len(seq1) * 100

    return identical, percentage_identity

def read_blosum62(filename):
    """
    Read a BLOSUM62 matrix file and store scores in a dictionary.
    Example key: ('A', 'R')
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    matrix_lines = []

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("#"):
            continue

        matrix_lines.append(line)

    amino_acids = matrix_lines[0].split()
    blosum = {}

    for line in matrix_lines[1:]:
        parts = line.split()
        row_amino_acid = parts[0]
        scores = parts[1:]

        for column_amino_acid, score in zip(amino_acids, scores):
            blosum[(row_amino_acid, column_amino_acid)] = int(score)

    return blosum


def calculate_blosum_score(seq1, seq2, blosum):
    """
    Calculate the total BLOSUM62 score for two sequences.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length for non-gapped alignment.")

    scores = []

    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]

        score = blosum[(aa1, aa2)]
        scores.append(score)

    total_score = sum(scores)
    average_score = total_score / len(scores)

    return total_score, average_score
human = read_fasta("human_dlx5.fasta.txt")
mouse = read_fasta("mouse_dlx5.fasta.txt")
random = read_fasta("random_289.fasta.txt")
blosum = read_blosum62("blosum62.txt")
print("Sequence lengths:")
print("Human:", len(human))
print("Mouse:", len(mouse))
print("Random:", len(random))
print()

comparisons = [
    ("human-mouse", human, mouse),
    ("human-random", human, random),
    ("mouse-random", mouse, random)
]

for name, seq1, seq2 in comparisons:
    identical, percentage = calculate_identity(seq1, seq2)
    blosum_total, blosum_average = calculate_blosum_score(seq1, seq2, blosum)

    print(name)
    print("Identical amino acids:", identical)
    print("Percentage identity:", round(percentage, 2), "%")
    print("BLOSUM62 score:", blosum_total)
    print("Average BLOSUM62 score per amino acid:", round(blosum_average, 2))
    print()