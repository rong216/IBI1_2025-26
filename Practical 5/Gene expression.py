import matplotlib.pyplot as plt

# Step 1: create a dictionary for gene expression
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

# Add a new gene
gene_expression["MYC"] = 11.6

# Print the dictionary
print("Gene expression dictionary:")
print(gene_expression)
print()

# Step 2: prepare data for bar chart
genes = list(gene_expression.keys())
expression_values = list(gene_expression.values())

# Draw bar chart
plt.figure(figsize=(8, 5))
plt.bar(genes, expression_values)

plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Level")

# Show value above each bar
for i in range(len(genes)):
    plt.text(genes[i], expression_values[i] + 0.2, round(expression_values[i], 1), ha="center")

plt.ylim(0, max(expression_values) + 2)
plt.show()

# Step 3: choose a gene of interest
gene_of_interest = "EGFR"   # you can change this to another gene

# Check whether the gene exists
if gene_of_interest in gene_expression:
    print("Expression level of", gene_of_interest, "is", gene_expression[gene_of_interest])
else:
    print("Error:", gene_of_interest, "is not in the dataset")

print()

# Step 4: calculate the average expression level
total = 0

for value in gene_expression.values():
    total = total + value

average_expression = total / len(gene_expression)

print("Average gene expression level:", round(average_expression, 2))