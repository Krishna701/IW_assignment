lst=[]
lst=input("Enter items in the list").split(',')


lst=list(dict.fromkeys(lst))
print(lst)
