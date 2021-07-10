import random
import math
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
    
# Linear Diophantine Equation
def LinearDiophantine(a, b):
    if EuclidsAlgorithm(a, b) == 1:
        print("The numbers " + str(a) + " and " + str(b) + " are relatively prime\nThe solution for the Linear Diophantine Equation " + str(a) + "x" + " + " + str(b) + "y = 1 is: ")
    else:
        print("The numbers " + str(a) + " and " + str(b) + " are not relatively prime")
        return 0
    
    # Initiating variables that will be used in the process
    d1 = 1
    d2 = 0
    r1 = 0
    r2 = 1
    x = a
    y = b
    sol1 = 0
    sol2 = 0
    
    # Iterating over the division of the numbers, this time recording the result of each floor division 
    while (x % y != 0):
        temp = x // y
        remainder = x % y
        x = y
        # Getting new numerator
        y = remainder
        # Calculating values
        temp2 = r1 - (r2 * temp)
        remainder = d1 - (d2 * temp)
        # Saving values to print the solution later
        d1 = d2
        r1 = r2
        d2 = remainder
        r2 = temp2
    sol1 = d2
    sol2 = r2

    print(str(a) + "*" + "("+str(sol1)+")" + " + " + str(b) + "*" + "("+str(sol2)+")" + " = 1")

def main():
    #LinearDiophantine(8, 2)
        
    LinearDiophantine(43, 486)
    LinearDiophantine(491, 599)
    LinearDiophantine(501, 896)
    LinearDiophantine(280, 5)
    LinearDiophantine(958, 933)
    LinearDiophantine(467, 652)
    LinearDiophantine(274, 584)
    LinearDiophantine(154, 179)
    LinearDiophantine(501, 562)
    LinearDiophantine(496, 33)

main()

"""while (temp != 0):
        if (c > d):
            # Remainder
            temp = c % d
            if (temp == 0):
                break
            # Saving result
            allR.append(c//d)
            # Getting new numerator
            c = temp
        elif (d > c):
            # Remainder
            temp = d % c
            if (temp == 0):
                break
            # Saving result
            allR.append(d//c)
            # Getting new numerator
            d = temp

    # Finding the solutions
    sol1 = 1
    for i in allR:
        sol1 = sol1 * i
        print(i)
    sol1 += 1
    sol2 = ((sol1 * min(a, b) - 1) / max(a, b)) * (-1)
"""
