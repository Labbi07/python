num=[ ]
while True:
    word=input("Enter a word ")
    if(word=="break"):
        break
    else:
        num.append(word)
def translate(x):
    d={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    return list(map(lambda word:d[word],x))
print(translate(num))
