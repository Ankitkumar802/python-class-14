while True:
    def setOrNot(number, n):
        mask = 1
        if (n & mask) == 1 or (n & mask) == 0:
            if number & (1 << (n-1)):
                print("SET")
            else:
                print("not set")
    number = int(input("enter a number"))
    n = int(input("enter the bit position"))
    setOrNot(number, n)