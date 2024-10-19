def numberofbits(n):
    ones = 0
    zeroes = 0
    while (n):
        if (n & 1 ==1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("numbers of ones =",ones, "/nnumber of zeroes=",zeroes)
number = int(input("enter your number:"))
numberofbits(number)
