from tkinter import *  
import tkinter
def helloCallBack():
    print("Name=",t1.get())
    i=radio.get()
    if i==1:
        print("Gender=Male")
    else:
        print("Gender=Female")
    j=chk1.get()
    k=chk2.get()
    l=chk3.get()
    str=""
    if j==1:
        str=str+" "+"Red"
    if k==2:
        str=str+" "+"Green"
    if l==3:
        str=str+" "+"Blue"
    print("Color=",str)
    for i in lb1.curselection():
        print(lb1.get(i))
    

base = Tk()  
base.geometry('600x600')  
base.title("Registration Form")  
l1 = Label(base, text="Enter Name",width=20,font=("bold", 10))
l1.place(x=90,y=55)  
t1 = Entry(base)
t1.place(x=220,y=55)

radio=IntVar()
l2= Label(base, text="Select Gender",width=20,font=("bold", 10))
l2.place(x=94,y=93)
r1 = Radiobutton(base, text="Male", value=1,variable=radio)
r1.place(x=220,y=93)
r2 = Radiobutton(base, text="Female", value=2,variable=radio)
r2.place(x=280,y=93)

l3= Label(base, text="Select Class",width=20,font=("bold", 10))
l3.place(x=90,y=123)
lb1 = Listbox(base)
lb1.insert(1, "MCA-I")
lb1.insert(2, "MCA-II")
lb1.insert(3, "MCA-III")
lb1.place(x=230,y=123)

chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
l4= Label(base, text="Select Color",width=20,font=("bold", 10))
l4.place(x=90,y=300)
c1 = Checkbutton(base,text = "Red",width = 20, onvalue=1,variable=chk1)
c1.place(x=220,y=300)
c2 = Checkbutton(base,text = "Green",width = 20,onvalue=2,variable=chk2)
c2.place(x=340,y=300)
c3 = Checkbutton(base,text = "Blue",width = 20,onvalue=3,variable=chk3)
c3.place(x=460,y=300)

b1 = Button(base, text ="Click", command = helloCallBack)
b1.place(x=190,y=380)
base.mainloop()  
