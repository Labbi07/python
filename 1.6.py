x=input('enter numbers:')
l=x.split()
s=0
m=1
for i in l:
    s=s+int(i)
for j in l:
    m=m*int(j)
print(m)
print(s)
