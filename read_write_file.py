f=open("C:\\data\\funny.txt","r")
f_out=open("C:\\data\\funny_wc.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write(line+"wordcount:"+str(len(tokens))+line)

f.close()
f_out.close()