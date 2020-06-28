def fun(n):
    return lambda u: u * n
output= fun(5)
print("result:",output(15))