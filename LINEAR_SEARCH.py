#for linear Search Algorithm program

x=[55,44,22,33,5,3,5,6]
n=int(input("enter number to search:"))
flag =0
for i in range(0,len(x)):
    if n==x[i]:
        flag=i+1
        break
if flag==0:
    print("number not found")
else:
    print("number found in",flag,"location")