'''

Write a Python program that produces truth tables for the logic gates AND, OR, NAND, NOR, XOR, and NOT.

'''
print ('+------------------------+')
print ('|\tAND TRUTH TABLE\t |')
print ('+------------------------+')
print ('| A\tB |\tA AND B\t |')
print ('+------------------------+')
a = True
b = True 

i = 0
for i in range(4):
    A = str(a)[0]
    B = str(b)[0]
    AND = a&b
    if i < 1:
        print('+', A, '\t', B, ' |\t', AND, '\t +')
    else:
        a = False
        print('+', A, '\t', B, ' |\t', AND, '\t +')
    b = not b
print ('+------------------------+')



print ('+------------------------+')
print ('|\tOR TRUTH TABLE\t |')
print ('+------------------------+')
print ('| A\tB |\tA OR B\t |')
print ('+------------------------+')
a = True
b = True 

i = 0
for i in range(4):
    A = str(a)[0]
    B = str(b)[0]
    OR = a|b
    if i < 1:
        print('+', A, '\t', B, ' |\t', OR, '\t+')
    else:
        a = False
        print('+', A, '\t', B, ' |\t', OR, '\t+')
    b = not b
print ('+------------------------+')

print ('+------------------------+')
print ('|\tNAND TRUTH TABLE |')
print ('+------------------------+')
print ('| A\tB |\tA NAND B |')
print ('+------------------------+')
a = True
b = True 

i = 0
for i in range(4):
    A = str(a)[0]
    B = str(b)[0]
    NAND = not a&b
    if i < 1:
        print('+', A, '\t', B, ' |\t', NAND, '\t +')
    else:
        a = False
        print('+', A, '\t', B, ' |\t', NAND, '\t +')
    b = not b
print ('+------------------------+')

print ('+------------------------+')
print ('|\tNOR TRUTH TABLE\t |')
print ('+------------------------+')
print ('| A\tB |\tA NOR B\t |')
print ('+------------------------+')
a = True
b = True 

i = 0
for i in range(4):
    A = str(a)[0]
    B = str(b)[0]
    NOR = not a|b
    if i < 1:
        print('+', A, '\t', B, ' |\t', NOR, '\t +')
    else:
        a = False
        print('+', A, '\t', B, ' |\t', NOR, '\t +')
    b = not b
print ('+------------------------+')

print ('+------------------------+')
print ('|\tXOR TRUTH TABLE\t |')
print ('+------------------------+')
print ('| A\tB |\tA XOR B\t |')
print ('+------------------------+')
a = True
b = True 

i = 0
for i in range(4):
    A = str(a)[0]
    B = str(b)[0]
    XOR = a!=b
    if i < 1:
        print('+', A, '\t', B, ' |\t', XOR, '\t +')
    else:
        a = False
        print('+', A, '\t', B, ' |\t', XOR, '\t +')
    b = not b
print ('+------------------------+')

print ('+------------------------+')
print ('|\tNOT TRUTH TABLE\t |')
print ('+------------------------+')
print ('| A\t |\tNOT A\t |')
print ('+------------------------+')
a = True

i = 0
for i in range(2):
    A = str(a)[0]
    NOT = not a
    print('+', A, '\t', '|\t', NOT, '\t +')
    a = not a
print ('+------------------------+')
        
        
        



