def summation():
    print("Please enter ")
    fT = input("First term of summation: ")
    cD = input("Common difference of sequence: ")
    n = input("Number of terms: ")
    print("The terms are: ")
    print(fT)
    newT = int(fT)
    i = 1
    while i < int(n):
        newT += int(cD)
        print(newT)
        i += 1
summation()