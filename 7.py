def String(List):  
    word_len = []  
    for i in List:  
        word_len.append((len(i), i))  
    word_len.sort()  
    return word_len[-1][1]  
  
print(String(["Hey", "Goodmorning", "Fine"]))