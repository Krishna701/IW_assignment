"""
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

String= input("Enter the string:")
# for i in String:
#     String[i]!= String[0]
#     i+=1
i=0
while String <= len(String):
    if String[i]==String[0]:
        String[i]='$'
    
print("Updated String: ",String) 