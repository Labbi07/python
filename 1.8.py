list1=[]
list2=[]
num=0
n=0
while num!=5:
    x=int(input("enter list1:"))
    list1.append(x)
    num=num+1
while n!=3:
        y=int(input("enter list2:"))
        list2.append(y)
        n=n+1
for i in list1:
    for j in list2:
        if i==j:
           flag=True
    else:
       flag=False
    break
print(flag)
