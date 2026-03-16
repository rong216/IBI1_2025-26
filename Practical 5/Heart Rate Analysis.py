import matplotlib.pyplot as plt

# Step 1: Define heart rate data and calculate basic statistics 
# Raw heart rate data
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)
# Calculate the number of patients (length of the tuple) and the mean heart rate
patient_count = len(heart_rates)
mean_heart_rate = sum(heart_rates) / patient_count  # Pure Python implementation
# mean_heart_rate = np.mean(heart_rates)  # numpy implementation

# Print the required sentence (1 decimal place)
print("=== Basic Heart Rate Statistics ===")
print(f"There are {patient_count} patients in the dataset, and the mean heart rate is {mean_heart_rate:.1f} bpm.")
print("-" * 30)

# Step 2: Heart Rate Classification Statistics
# Initialize counters
low = 0
normal = 0
high = 0

# Iterate through heart rate data and count by category
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:  # > 120
        high += 1

# Store classification results (for later plotting/printing)
hr_categories = ['Low Heart Rate', 'Normal', 'High Heart Rate']
hr_counts = [low, normal, high]

# Print classification counts
print("=== Heart Rate Classification Results ===")
print(f"Low Heart Rate (<60 bpm): {low} patients")
print(f"Normal (60-120 bpm): {normal} patients")
print(f"High Heart Rate (>120 bpm): {high} patients")

# Find the largest category
max_count = max(hr_counts)
max_index = hr_counts.index(max_count)
max_category = hr_categories[max_index]
# Print the largest category sentence
print(f"The category with the largest number of patients is: {max_category}")
print("-" * 30)

# Step 3: Plot Heart Rate Classification Pie Chart
plt.figure(figsize=(7, 7))  # A square canvas is recommended for pie charts
# Plot pie chart: autopct shows percentage, explode highlights the largest category, shadow adds shadow effect
explode = [0.1 if x == max_count else 0 for x in hr_counts]  # Highlight the largest category
plt.pie(hr_counts, labels=hr_categories, autopct='%1.1f%%', 
        explode=explode, shadow=True, startangle=90,
        colors=['lightcoral', 'lightgreen', 'lightskyblue'])
# Add title
plt.title('Distribution of Resting Heart Rate Categories', fontsize=14)
# Ensure the pie chart is a perfect circle
plt.axis('equal')
# Save the image
plt.savefig('heart_rate_pie.png', dpi=300, bbox_inches='tight')
# Display the chart
plt.show()
print("=" * 50)

