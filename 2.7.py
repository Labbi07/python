a=input("emter ")
def pangram(a):
    alph="abcdefghijklmnopqrstuvwxyz"
    for i in alph:
      if i not in a:
        return False
    return True
print(pangram(a))

