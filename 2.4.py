def find_longest_word(list1):
    length = 0
    #word_long = 0
  #  for word in list1:
      # if len(word) > length:
          # length = len(word)
          # word_long = word
   
    #return length,word_long
    word_long=list(map(lambda word:len(word),list1))
    return max(word_long)
num=[]
while True:
    word=input("Enter a word ")
    if(word=="break"):
        break
    else:
        num.append((word))
print(find_longest_word(num))
