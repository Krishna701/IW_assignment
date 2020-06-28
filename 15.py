symbol= input("Enter a pair of symbols such as [],{},<>: ")
string=input("Insert string:")
print( symbol[:2] + string + symbol[2:])


def insert(symbol , string):
    return symbol[:2] + string + symbol[2:]

print(insert('[[]]', 'Python'))
print(insert('{{}}', 'PHP'))
print(insert('<<>>', 'HTML'))
    