# Define the solution
def isSubset(a, b):
    if a.intersection(b) == a:
        return True
    else:
        return False
        
# Initiate variables
a = {3, 7, 8, 42}
b = {1, 3, 5, 7, 6, 8, 34, 42}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 34, 40, 42}

print("Is a subset of b?", isSubset(a, b))
print("Is b subset of a?", isSubset(b, a))
print("Is b subset of c?", isSubset(b, c))
print("What's the union of a and b? It is: ", a.union(b))
print("What's the intersection of a and c? It is:", a.intersection(c))
print("What's the difference of b and c? The difference is:", c - b) # or c.difference(b) 
print("What's the symmetrical difference of a and b? It is:", b.symmetric_difference(a))