'''

Write a Python program that produces a truth table for the following statements:

- p and q
- p or q
- if p, then q
- p if and only if q

'''
print ('+-----------------------------------------------+')
print ('+  p\t q  |\tp^q\tpvq\tp->q\tp<-->q  +')
print ('+-----------------------------------------------+')
p = True
q = True 

i = 0
for i in range(4):
    P = str(p)[0]
    Q = str(q)[0]
    pndq = str(p & q)[0]
    pvq = str(p | q)[0]
    pifq = str(q if p else True)[0]
    piffq = str(True if p==q else False)[0]
    if i < 1:
        print('+ ', P, '\t', Q, ' |\t', pndq, '\t',pvq, '\t', pifq, '\t  ', piffq, '\t+')
    else:
        p = False
        print('+ ', P, '\t', Q, ' |\t', pndq, '\t',pvq, '\t', pifq, '\t  ', piffq, '\t+')
    q = not q
print ('+-----------------------------------------------+')        


        
        
        


