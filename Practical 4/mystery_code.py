# What does this code do:
# This program generates 11 random numbers (from 1 to 10)
# and calculates their total sum

# Import function
from random import randint

# Step 1: initialize variables
total = 0
count = 1

# Step 2: while loop (run 11 times)
while count <= 11:
    
    # generate random number
    number = randint(1, 10)
    
    # add to total
    total = total + number
    
    # print each step (optional but clearer)
    print("Iteration", count, "- Random number:", number)
    
    # update counter
    count = count + 1

# Step 3: output final result
print("Total sum:", total)