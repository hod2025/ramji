n = int(input("Enter the number of Fibonacci terms: "))
fibo = [0, 1]

for i in range(2, n):
    rev = fibo[-1] + fibo[-2]
    fibo.append(rev)    
print("Fibonacci sequence:", fibo)


#fibonacci sum
def fibonacci(n):
    if n<0:
        print("enter the input")
    elif n==0:
        return 0
    elif n ==1 or n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n-2)
n=int(input("enter the number:"))
print(fibonacci(n))