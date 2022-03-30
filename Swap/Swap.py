with open ("sample1.txt", "r" ) as a:
    temp1 = a.read()

with open ("sample2.txt", "r" ) as b:
    temp2 = b.read()

with open ("sample1.txt", "w" ) as a:
    a.write(temp2)

with open ("sample2.txt", "w" ) as a:
    a.write(temp1)

    
