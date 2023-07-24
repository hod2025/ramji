def divide(x,y):
    try:
        res=x//y
    except ZeroDivisionError:
        print("can't divide by zero")
    else:
        print("yeah your answers is:",res)
    finally:
        print("this block always executed")
divide(3,2)
divide(3,0)

try:
    x=int(input("enter the number:"))
    y=int(input("enter the number:"))
    res=x//y
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("yeah ! your answers is :",res)
finally:
    print("this is always excuted")