size = int(input("Enter the size of the pattern: "))
while True:
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()
    break 