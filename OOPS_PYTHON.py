class Parent:	# define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")
    def parentMethod(self):
        print ("Calling parent method")
    def setAttr(self, attr):
        self.parentAttr = attr
    def getAttr(self):
        print ("Parent attribute :", self.parentAttr)
    
class Child(Parent): # define child class
    def __init__(self):
        print ("Calling child constructor")
    def childMethod(self):
        print ("Calling child method")
    
c = Child()
c.childMethod() 
c.parentMethod() 
c.setAttr(200) 
c.getAttr()
