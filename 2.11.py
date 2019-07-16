with open("C:\\Users\\prmogili\\Desktop\\1.txt") as f:
    with open("C:\\Users\\prmogili\\Desktop\\2.txt","w") as f1:
        for line in f:
            f1.write(line)
    f1=open("C:\\Users\\prmogili\\Desktop\\2.txt","r")
    print(f1.read())

