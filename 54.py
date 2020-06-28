
def unique(lst):
    uniq_lst=set(lst)
    lst1=list(uniq_lst)
    
    for x in lst1:
        print(x)

lst=[1,2,3,3,3,3,4,5]
print("Unique elements: ", lst)  