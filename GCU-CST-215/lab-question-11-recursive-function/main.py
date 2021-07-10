'''
3a(n+1) - 4a(n) = 0

Explicit formula found:
a(n) = 5 * (4/3)^n-1
Let's test it

'''

def Explicit(i):
    n = 1
    while (n <= i):
        an = 5 * pow(4/3, n-1)
        print(round(an, 2))
        n += 1

def Recursive(n):
    if (n > 0):
        an = 5 * pow(4/3, n-1)
        print(round(an, 2))
        Recursive(n-1)

'''print("Recursive: ")
Recursive(20)

print("Explicit: ")
Explicit(20) '''

def ExplicitFormula(n):
    an = 5 * pow(4/3, n-1)
    return(round(an, 2))

def RecursiveFormula(n):
    an = ExplicitFormula(n+1) * 3 / 4
    return(round(an, 2))

print("Recursive \t Explicit \n-------------------------")
i = 1
while(i <= 20):
    print(RecursiveFormula(i), "\t\t", ExplicitFormula(i))
    i += 1





















