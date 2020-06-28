lst=[]
number=int(input("Enter number of items in a list: "))
for i in range(number):
    num=int(input("num:"))
    lst.append(num)
print("The sum of numbers is: ", sum(lst))