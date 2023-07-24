#for Binary Search Algorithm program


list=[10,20,30,40,50,60,70,80,90]
n=int(input("enter element to search"))
first=0
last = len(list)-1
while first<=last:
    mid=(first+last)//2
    if list[mid]==n:
        print("number is in",mid+1,"location")
        break
    elif list[mid]>n:
        last=mid-1
    else:
        first=mid+1
if first> last:
    print("number not found in the list")