x=int(input("enter size of list:"))
l=[]
n=0
while n<x:
    m=int(input("enter numbers:"))
    l.append(m)
    n=n+1
def max_in_list(l):
    j=0
    for i in l:
        if i>j:
            j=i
    print(j)
max_in_list(l)

