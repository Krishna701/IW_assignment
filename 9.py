a=input("Enter the string: ")
if len(a)<=2:
     print(a)
else:
     print(a[-1]+a[1:-1]+a[0])
#print(a if len(a)<=2 else print(a[-1]+a[1:-1]+a[0]))