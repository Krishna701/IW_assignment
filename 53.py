def upper_lower(string):
    a={"upper_case": 0, "lower_case": 0}
    for i in string:
        if i.isupper():
            a["upper_case"] += 1
        elif i.islower():
            a["lower_case"] += 1
        else:
            pass
        
    print("String: ", string)
    print("lowercase letters :", a["lower_case"])
    print("Uppercase letters :", a["upper_case"])

string=input("Enter the string:")
upper_lower(string)