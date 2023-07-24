#armstrong number
num = int(input("enter the number:"))
temp=num
sum=0
while temp>0:
    dig=temp%10
    sum += dig**3
    temp//=10
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong no")