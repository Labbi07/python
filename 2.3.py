num=[ ]
while True:
    word=input("Enter a word ")
    if(word=="break"):
        break
    else:
        num.append(word)
print(list(map(lambda word:len(word),num)))
