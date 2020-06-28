"""
Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

a,b=input("Enter two strings: ").split(',')
print(a)
print(b)
print(b[:2]+a[2:],a[:2]+b[2:])
# print(b[:2]+a[2:])
