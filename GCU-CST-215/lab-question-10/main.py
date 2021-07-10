# This is my own work

def CollatzSequence(C0):
    count = 1
    Cn = C0
    while (Cn != 1):
        if (Cn % 2 != 0):
            Cn = Cn * 3 + 1
        else:
            Cn = Cn/2
        count += 1
    print("C[0] = " + str(C0) + " has " + str(count) + " terms")
    
CollatzSequence(65)
CollatzSequence(66)
CollatzSequence(67)
CollatzSequence(98)
CollatzSequence(99)
CollatzSequence(100)
CollatzSequence(101)
CollatzSequence(102)
CollatzSequence(4585418)
CollatzSequence(4585419)
    