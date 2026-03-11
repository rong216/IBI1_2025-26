# What does this piece of code do?
# Answer: This code loops 11 times (from 1 to 11), generates a random integer between 1 and 10 each time, accumulates the values, and finally outputs the total sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint  # Import the randint function from the random library to generate random integers within a specified range

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil  # Import the ceil function from the math library to round a number up to the nearest integer

total_rand = 0  # Initialize an accumulator variable to store the sum of all random numbers, starting at 0
progress = 0  # Initialize a loop counter variable to record the current number of loop iterations, starting at 0
while progress <= 10:  # Continue executing the loop body when the number of iterations does not exceed 10 (executes 11 times total: progress from 0 to 10)
    progress += 1  # Increment the counter variable by 1 each loop to update the current number of iterations
    n = randint(1, 10)  # Generate a random integer between 1 and 10 (inclusive) and assign it to variable n
    total_rand += n  # Add the generated random integer n to the total sum variable total_rand

print(total_rand)  # After the loop ends, output the total sum of all random integers (total_rand)