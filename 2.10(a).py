def add(num):
    y=0
    for x in num:
        y=(y+x);
    return y
def sub(num):
    y=0
    for x in num:
        y=(x-y);
    return y
def sort(num):
    for x in range(0,len(num)):
        for y in range(0,len(num)):   
            if((num[y])<(num[x])):
                t=num[y]
                num[y]=num[x]
                num[x]=t
    return num
def max(num):
    maxi=num[0]
    for x in num:
        if(x>maxi):
            maxi=x
    return maxi
def min(num):
    mini=num[0]
    for x in num:
        if(x<mini):
            mini=x
    return mini

