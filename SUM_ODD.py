#sum of odd numbers
min=int(input("enter the minimum:"))
max=int(input("enter the maximum:"))
sum=0
for i in range(min,max+1):
    if i%2!=0:
        print(i)
        sum+=i
print("sum of odd number:",sum)