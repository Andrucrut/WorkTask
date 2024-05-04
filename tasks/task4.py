def printTable(num):
    print("  ", end="")
    for i in range(1, num+1):
        print(str(i).rjust(3), end="")
    print()

    for i in range(1, num+1):
        print(str(i).rjust(2), end="")
        for j in range(1, num+1):
            print(str(i*j).rjust(3), end="")
        print()

printTable(5)
