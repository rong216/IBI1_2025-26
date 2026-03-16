import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Step 1: Create and extend the gene expression dictionary 
# Initial dictionary: 5 genes + expression levels
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
# Add new gene MYC with expression level 11.6
gene_expression['MYC'] = 11.6
# Print the dictionary (verify correct creation/extension)
print("=== Gene Expression Dictionary ===")
print(gene_expression)
print("-" * 30)

# Step 2: Plot Gene Expression Bar Chart 
# Extract x-axis (gene names) and y-axis (expression levels)
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())

# Create figure
plt.figure(figsize=(8, 5))
plt.bar(genes, expressions, color='lightblue', edgecolor='black')

plt.title('Gene Expression Levels in Biological Sample', fontsize=14)
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)

for x, y in zip(genes, expressions):
    plt.text(x, y + 0.2, f'{y}', ha='center', fontsize=10)

plt.ylim(0, max(expressions) + 1)

plt.savefig('gene_expression_bar.png', dpi=300, bbox_inches='tight')

plt.show()

# Step 3: Query the expression level of the target gene
gene_of_interest = 'EGFR'  # Example: Query EGFR, can be changed to 'TP53'/'ABC' (non-existent gene)

# Exception handling: Check if the gene exists in the dictionary
if gene_of_interest in gene_expression:
    print(f"=== Target Gene Expression Level ===")
    print(f"Gene {gene_of_interest} expression level: {gene_expression[gene_of_interest]}")
else:
    print(f"=== Error Message ===")
    print(f"Gene {gene_of_interest} is not present in the dataset!")
print("-" * 30)

# Step 4: Calculate the average gene expression 
# Method 1: Pure Python implementation (Recommended, no additional library dependencies)
total_express = sum(gene_expression.values())
gene_count = len(gene_expression)
avg_express = total_express / gene_count

# Method 2: numpy implementation (Simpler, requires numpy import)
# avg_express = np.mean(list(gene_expression.values()))

# Print the average value (formatted to 2 decimal places for better readability)
print("=== Average Gene Expression ===")
print(f"Total genes: {gene_count}")
print(f"Average gene expression level: {avg_express:.2f}")
print("=" * 50)
