# Generate sets
for i in range(3):
    # Generate random numbers
    for j in range(3):
        if j == 0:
            a = randint(0, 100)
        elif j == 1:
            b = randint(0, 100):
        else
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