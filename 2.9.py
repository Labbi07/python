def Char_Freq(string): 
  
    # Creating an empty dictionary  
    freq = {} 
    for i in string: 
        if (i in freq): 
            freq[i] += 1
        else: 
            freq[i] = 1
      for key, value in freq.items(): 
        print ("%c : %d"%(key, value),end=' ') 
  Char_Freq("abbabcbdbabdbdbabababcbcbab")
