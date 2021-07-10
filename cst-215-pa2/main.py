from random import randint

# Generate sets
for i in range(3):
    # Generate random numbers
    for j in range(3):
        if j == 0:
            a = randint(0, 100)
        elif j == 1:
            b = randint(0, 100)
        else:
            c = randint(0, 100)
    # Populate sets with random int
    if i == 0:
        set1 = set((a, b, c))
    elif i == 1:
        set2 = set((a, b, c))
    else:
        set3 = set((a, b, c))

# Display the random populated sets
print(set1, "\n", set2, "\n", set3)

# Now generate the cartesian product of the sets
CP = set()

for i in set1:
    for j in set2:
        for k in set3:
            
            # Create a list to put the sets inside
            Triple = []
            # Add each random number to the list
            Triple.append(i)
            Triple.append(j)
            Triple.append(k)
            
            CP.add(tuple(Triple))
            
print(CP)
            

