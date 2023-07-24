#for string
string=input("enter the string")
if string==string[::-1]:
    print("the string is a palindrom")
else:
    print("the string is not palindrom")
    
    
#for integer number
num=int(input("enter the number"))
temp=num
rev=0
while(temp>0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print(num,"is palindrom")
else:
    print(num,"is not a palindrom")