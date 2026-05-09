# Practical 8 - Predicting protein mass.py
# Pseudocode:
# 1. Store the masses of the 20 amino acids in a dictionary
# 2. Define a function that takes a protein sequence
# 3. Check whether each amino acid is valid
# 4. Add the masses together
# 5. Return the total protein mass
# 6. Include an example function call

amino_acid_masses = {
    "G": 57.02,
    "A": 71.04,
    "S": 87.03,
    "P": 97.05,
    "V": 99.07,
    "T": 101.05,
    "C": 103.01,
    "I": 113.08,
    "L": 113.08,
    "N": 114.04,
    "D": 115.03,
    "Q": 128.06,
    "K": 128.09,
    "E": 129.04,
    "M": 131.04,
    "H": 137.06,
    "F": 147.07,
    "R": 156.10,
    "Y": 163.06,
    "W": 186.08
}


def calculate_protein_mass(sequence):
    sequence = sequence.upper().strip()
    total_mass = 0

    for amino_acid in sequence:
        if amino_acid in amino_acid_masses:
            total_mass += amino_acid_masses[amino_acid]
        else:
            print(f"Error: undefined amino acid = {amino_acid}")
            return None

    return total_mass


if __name__ == "__main__":
    # Example function call
    user_sequence = input("Please enter an amino acid sequence: ")
    result = calculate_protein_mass(user_sequence)

    if result is not None:
        print(f"Sequence: {user_sequence.upper()}")
        print(f"Total protein mass: {result:.2f} amu")