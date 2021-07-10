def countBits(x):
    # Variable for the binary representation
    c = ""
    
    # Temporary Variable
    temp = 0
    
    # Number of 1s
    n1 = 0
    
    # Iteration over the numebr for results
    while (x > 0):
        temp = x%2
        if temp == 1:
            n1 += 1
        c = str(temp) + c 
        x = int(x/2)
    print(c,"\t",n1)
    
countBits(12)