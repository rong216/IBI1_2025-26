# Pseudocode: IBI1 Class Infection Rate Simulation
# 1. Define initial variables: initial number of infected people, daily growth rate, total class population n=91, initial days=0
# 2. Print header to display daily infected numbers
# 3. Use a loop (while) to calculate the next day's infected number as long as current infected < 91
# 4. Daily infected number = previous day's infected number × (1 + growth rate)
# 5. Increment days by 1 each time, print the current day and infected number
# 6. Exit the loop when infected ≥91, print total days

# Actual Code
initial_infected = 5  # Initial number of infected people
growth_rate = 0.4     # Daily growth rate 40%
total_students = 91   # Total number of students in the class
current_infected = initial_infected
days = 0

print("IBI1 Class Infection Rate Simulation")
print(f"Day {days+1}, Number of infected people: {round(current_infected)}")

# While loop to calculate daily infected numbers
while current_infected < total_students:
    current_infected = current_infected * (1 + growth_rate)
    days += 1
    print(f"Day {days+1}, Number of infected people: {round(current_infected):.1f}")  

# Loop ends, print total days
print(f"\nIt took a total of {days+1} days for all {total_students} people to be infected")