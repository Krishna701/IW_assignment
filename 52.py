def ranges(n):
    if n in range(1,9):
        print(f"{n} is in range.")
    else:
        print(f"{n} is not in range")
n=int(input("Enter the number: "))
ranges(n)