def copy(lst):
    lst_copy=[]
    lst_copy.extend(lst)
    return lst_copy
        

lst=input("Enter the list: ").split(',')
lst_copy=copy(lst)
print("first: ", lst)
print("copied: ",lst_copy)