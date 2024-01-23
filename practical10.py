fh = open('practical10.txt','w')
Num=int(input("Enter a Number: ")) 
abc=[] 
while Num>0: 
    temp=Num%2 
    abc.append(temp) 
    Num=int(Num/2) 
abc.reverse() 
fh.write(str(abc))
fh.close()