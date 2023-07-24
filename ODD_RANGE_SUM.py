max=int(input("enter the maximum number"))
odd=0
for number in range(1,max+1,2):
    print("{0}".format(number))
    odd += number
print("the sum of Odd NUmbers from 1 to {0} = {1}".format(max,odd))
