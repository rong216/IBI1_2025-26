import matplotlib.pyplot as plt

# Step 1: define heart rate data
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)

# calculate number of patients
count = len(heart_rates)

# calculate mean heart rate
total = 0
for hr in heart_rates:
    total = total + hr

mean = total / count

# print result
print("Number of patients:", count)
print("Mean heart rate:", round(mean, 1), "bpm")
print()

# Step 2: classification
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

print("Low heart rate:", low)
print("Normal:", normal)
print("High heart rate:", high)

# find largest category
counts = [low, normal, high]
labels = ["Low", "Normal", "High"]

max_value = max(counts)
max_index = counts.index(max_value)

print("Largest category:", labels[max_index])
print()

# Step 3: pie chart
plt.figure(figsize=(6, 6))

plt.pie(counts, labels=labels, autopct="%1.1f%%")

plt.title("Heart Rate Distribution")

plt.axis("equal")

plt.show()