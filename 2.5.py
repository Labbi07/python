def filter_long_words(list1,n):
    word_long=list(filter(lambda word:len(word)>n ,list1))
    return word_long
num=[]
n=int(input("Enter a number "))
while True:
    word=input("Enter a word ")
    if(word=="break"):
        break
    else:
        num.append((word))
print(filter_long_words(num,n))
