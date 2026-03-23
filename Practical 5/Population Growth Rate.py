import matplotlib.pyplot as plt

# Step 1: define population data
population = {
    "UK": (66.7, 69.2),
    "China": (1426, 1410),
    "Italy": (59.4, 58.9),
    "Brazil": (208.6, 212.0),
    "USA": (331.6, 340.1)
}

# Step 2: calculate percentage change
pop_change = {}

for country in population:
    pop2020 = population[country][0]
    pop2024 = population[country][1]
    
    change = (pop2024 - pop2020) / pop2020 * 100
    pop_change[country] = round(change, 2)

# Step 3: print original results
print("Population change (%):")
for country in pop_change:
    print(country, ":", pop_change[country], "%")

print()

# Step 4: sort from largest to smallest
sorted_list = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)

print("Sorted population change (%):")
for country, change in sorted_list:
    print(country, ":", change, "%")

print()

# Step 5: find largest increase and decrease
largest_increase = sorted_list[0]
largest_decrease = sorted_list[-1]

print("Largest increase:", largest_increase[0], largest_increase[1], "%")
print("Largest decrease:", largest_decrease[0], largest_decrease[1], "%")

print()

# Step 6: prepare data for plotting
countries = []
changes = []

for item in sorted_list:
    countries.append(item[0])
    changes.append(item[1])

# Step 7: plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(countries, changes)

plt.title("Population Change (2020-2024)")
plt.xlabel("Country")
plt.ylabel("Change (%)")

# add value labels
for i in range(len(countries)):
    plt.text(countries[i], changes[i], round(changes[i], 2), ha="center")

# add zero line
plt.axhline(0)

plt.show()