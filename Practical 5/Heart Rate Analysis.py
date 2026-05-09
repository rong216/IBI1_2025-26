import matplotlib.pyplot as plt

# Practical 5 - Heart Rate Analysis
# Pseudocode:
# 1. Store the heart rate data
# 2. Calculate the number of patients and the mean heart rate
# 3. Count how many heart rates are low, normal, and high
# 4. Identify the largest category
# 5. Plot a pie chart of the category distribution

# Step 1: define heart rate data
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)

# Step 2: calculate number of patients and mean heart rate
count = len(heart_rates)

total = 0
for hr in heart_rates:
    total = total + hr

mean = total / count

# Step 3: classification
low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low = low + 1
    elif hr <= 120:
        normal = normal + 1
    else:
        high = high + 1

# Step 4: find largest category
counts = [low, normal, high]
labels = ["Low", "Normal", "High"]

max_value = max(counts)
max_index = counts.index(max_value)

# Print results
print(f"There are {count} patients in the dataset, and the mean heart rate is {mean:.1f} bpm.")
print(f"There are {low} patients in the low category, {normal} in the normal category, and {high} in the high category.")
print(f"The largest category is {labels[max_index]} with {max_value} patients.")
print()

# Step 5: pie chart
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct="%1.1f%%")
plt.title("Heart Rate Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()