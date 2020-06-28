attribute = [('Python', 0), ('language',5),('Programming', 4), ('is a', 2), ('fun', 3)]
print("Original list of tuples:")
print(attribute)
attribute.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(attribute)