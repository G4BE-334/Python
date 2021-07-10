import random
# importing random function to use randint

# Defining the algorithm to calculate GCD
def EuclidsAlgorithm(x, y):
    
    # Iterate over x and y until one of the remainder = 0, meaning they're divisible
    # Or until x = y 
    while (x > 0 and y > 0):
        if (x > y):
            x = x % y
        elif (y > x):
            y = y % x
        else:
            return(x)
    return(max(x, y))
    
print(EuclidsAlgorithm(15, 5))
# Generate 100 random pairs between 1 and 9999999 and calculating their GCD
for i in range(100):
    a = random.randint(1, 9999999)
    b = random.randint(1, 9999999)
    
    # Printing results
    print(a, " \t ", b, " \t ", EuclidsAlgorithm(a, b), "\n")
