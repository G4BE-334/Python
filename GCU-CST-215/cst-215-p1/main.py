# Print the structure of the half-adder table
print('Half-Adder')

# Half-Adder function
def HalfAdder(i, j):
    # Analyse the 3 cases of sum and carry
    if (i + j == 0):
        s = 0
        c = 0
    elif (i + j == 1):
        s = 1
        c = 0
    elif (i + j == 2):
        s = 0
        c = 1
        
    # Print out the rest of the table
    print('i = ', i, ' j = ', j, ' | ', ' c = ', c, ' s = ', s)
    
    return (s, c)

# Calling the function to populate the table
HalfAdder(0, 0)
HalfAdder(0, 1)
HalfAdder(1, 0)
HalfAdder(1, 1)

# Print the structure of the full-adder table
print('Full-Adder')

# Full-Adder function
def FullAdder(i, j, k):
    # Analyse the 4 cases of sum and carry
    if (i + j + k == 0):
        s = 0
        c = 0
    elif (i + j + k == 1):
        s = 1
        c = 0
    elif (i + j + k == 2):
        s = 0
        c = 1
    elif (i + j + k == 3):
        s = 1
        c = 1
        
    print('i = ', i, ' j = ', j, ' k = ', k, ' | ', ' c = ', c, ' s = ', s)
    return (s, c)
    
# Calling the function to populate the table
FullAdder(0, 0, 0)
FullAdder(0, 0, 1)
FullAdder(0, 1, 0)
FullAdder(0, 1, 1)
FullAdder(1, 0, 0)
FullAdder(1, 0, 1)
FullAdder(1, 1, 0)
FullAdder(1, 1, 1)

def ParallelAdder(ABC, DEF):
    # Defining variables
    i = 2
    c = 0
    s = 0
    WXYZ = ''
    while (i >= 0):
        # Analysing which of the 4 FullAdder cases it is for each "column" of the sum
        if (int(ABC[i]) + int(DEF[i]) + c == 0):
            s = 0
            c = 0
        elif (int(ABC[i]) + int(DEF[i]) + c == 1):
            s = 1
            c = 0
        elif (int(ABC[i]) + int(DEF[i]) + c == 2):
            s = 0
            c = 1
        elif (int(ABC[i]) + int(DEF[i]) + c == 3):
            s = 1
            c = 1
            
        # Update 1 so we don't have an infinite loop
        i -= 1
        # Add each digit to the string WXYZ that represents the binary number result
        WXYZ = str(s) + WXYZ
    
    # Adding the last carry that represents the far left digit
    WXYZ = str(c) + WXYZ
    
    # Print the result
    print(ABC, ' + ', DEF, ' = ', WXYZ)
    
# Calling the function
ParallelAdder('011', '110')
        
        











