x=[]
num=0
while num!=4:
    a=int(input("enter number:"))
    x.append(a)
    num=num+1
b=int(input("enter the number to be found"))
for k in x:
    if b==k:
          flag=True
          break
    else:
          flag=False
print(flag)
