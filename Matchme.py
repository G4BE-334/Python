import numpy as np
# Vectors
A = np.array([6, 5, 9, 4, 8, 9, 9, 6, 8, 8, 10, 9, 7, 8, 7])
B = np.array([7, 8, 8, 4, 8, 7, 10, 9, 7, 8, 7, 8, 8, 6, 8])
Threshold = 15

# Manually compute cosine similarity
dot = np.dot(A, B)
norma = np.linalg.norm(A)
normb = np.linalg.norm(B)
cos = dot / (norma * normb)
angle = np.rad2deg(np.arccos(cos))

# Display calculations results
print("dot : %8.2f" % dot)
print("norma : %8.2f" % norma)
print("normb : %8.2f" % normb)
print("cos : %8.2f" % cos)
print("angle : %8.2f degrees" % angle)

# Test for match based on threshold
if angle < Threshold:
    print("Good match! The threshold is: ", Threshold)
else:
    print("Not a good match :( The threshold is: ", Threshold)
