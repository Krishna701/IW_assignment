def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s = "Python programming"
  
print ("The original string : ",s) 

print ("The reversed string : ",reverse(s)) 