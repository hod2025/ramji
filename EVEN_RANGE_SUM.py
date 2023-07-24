max=int(input("please enter the maximum number:"))
even=0
for number in range(1,max+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        even+=number
print("the sum of even numbers from 1 to {0}= {1}".format(max,even))