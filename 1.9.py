list=[]
n=0
while n!=3:
    a=int(input("enter values to print status:"))
    list.append(a)
    n=n+1
for i in list:
    for i in range(0,i):
        print("*",end= ' ')
    print("\n")
