a=input("enter the sentence: ")
counts = dict()
words = a.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)