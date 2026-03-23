# Step 1: define initial variables
initial_infected = 5
growth_rate = 0.4
total_students = 91

current_infected = initial_infected
day = 1

# Step 2: print header
print("IBI1 Class Infection Rate Simulation")
print("Day", day, "- Infected:", current_infected)

# Step 3: while loop
while current_infected < total_students:
    
    # Step 4: calculate next day
    current_infected = current_infected * (1 + growth_rate)
    
    # Step 5: update day
    day = day + 1
    
    # Step 6: print result
    print("Day", day, "- Infected:", round(current_infected, 1))

# Step 7: final result
print("It took", day, "days for all", total_students, "students to be infected")