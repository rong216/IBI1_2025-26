import matplotlib.pyplot as plt
# Step 1: Define population data and calculate percentage change 
# Population dictionary: key = country, value = (population 2020, population 2024) Unit: millions
population = {
    'UK': (66.7, 69.2),
    'China': (1426, 1410),
    'Italy': (59.4, 58.9),
    'Brazil': (208.6, 212.0),
    'USA': (331.6, 340.1)
}

# Initialize dictionary to store percentage changes
pop_change = {}
# Iterate and calculate percentage change for each country (rounded to 2 decimal places)
for country, (pop2020, pop2024) in population.items():
    change = (pop2024 - pop2020) / pop2020 * 100
    pop_change[country] = round(change, 2)

# Print percentage change for each country
print("=== Population Percentage Change by Country (2020-2024) ===")
for country, change in pop_change.items():
    print(f"{country}: {change}%")
print("-" * 30)
# Step 2: Sort and find countries with largest increase and decrease  
# Convert dictionary to list and sort in descending order by percentage change (key=lambda x: x[1])
sorted_pop_change = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
print("=== Population Percentage Change (Sorted from Largest to Smallest) ===")
for country, change in sorted_pop_change:
    print(f"{country}: {change}%")

# Find countries with the largest increase and largest decrease
largest_increase = sorted_pop_change[0]  # First after sorting: largest increase
largest_decrease = sorted_pop_change[-1] # Last after sorting: largest decrease

# Print result statements
print(f"\nCountry with the largest population increase: {largest_increase[0]} ({largest_increase[1]}%)")
print(f"Country with the largest population decrease: {largest_decrease[0]} ({largest_decrease[1]}%)")
print("-" * 30)

# Step 3: Plot population change bar chart  
import os  # New import

# Extract sorted x-axis (countries) and y-axis (percentage change)
sorted_countries = [x[0] for x in sorted_pop_change]
sorted_changes = [x[1] for x in sorted_pop_change]

# Set colors: positive values = blue, negative values = red
colors = ['blue' if c > 0 else 'red' for c in sorted_changes]

# Create figure
plt.figure(figsize=(9, 6))
# Plot bar chart
plt.bar(sorted_countries, sorted_changes, color=colors, edgecolor='black')

# Add labels (well-labelled)
plt.title('Population Percentage Change (2020-2024) by Country', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population Percentage Change (%)', fontsize=12)
# Add horizontal zero line (highlight growth / decrease)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
# Display value labels
for x, y in zip(sorted_countries, sorted_changes):
    plt.text(x, y + 0.1 if y > 0 else y - 0.3, f'{y}%', ha='center', fontsize=10)

# Automatically create folder and save the figure
os.makedirs('Practical 5', exist_ok=True)
plt.savefig('Practical 5/population_change_bar.png', dpi=300, bbox_inches='tight')
# Show the plot
plt.show()