def num(lst):
    even=[]
    for i in lst:
        if i%2 == 0: 
            even.append(i)
        
    return even

lst=[1,2,3,4,5,6,7,8]
print("Even numbers: ", num(lst))