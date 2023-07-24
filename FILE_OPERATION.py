f=open("myfile.txt","w")
f.write("create a new text file !")
print("write successfully")
f.close()

f=open("myfile.txt")
f.read()

f=open("myfile.tx
       t",'a')
f.write("append this text")

f=open("myfile.txt")
f.read()