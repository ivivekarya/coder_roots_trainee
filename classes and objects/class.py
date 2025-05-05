# import test

# test.checkAnswer()

# constructor -- constructor is used to initialize or assign values to the data members(variables) of the class, and is called or invoked automatically when an object of the class is created

# member function -- function in class
# contructor in python--  __init__ 

class Students():
    # print("Hello")
    # def __init__ (self,a,b):
    #     # print("Hello this is contructor",a)
    #     # print("in constr",self)
        
    #     self.name=a
    #     self.roll=b
    #     print(self.name,b)
    def __init__ (self):
        # print("Hello this is contructor",a)
        # print("in constr",self)
        pass
        
        # self.name=input("Enter Name ")
        # self.roll=input("Enter Roll No ")
        # print(self.name,self.roll)
        
    def inputVal(self):
        self.name=input("Enter Name ")
        self.roll=input("Enter Roll No ")
    def printVal(self):
        print(f"Name is {self.name} and roll no is {self.roll} ")
        

        

# st1= Students("Gurminder",12)
# stu2=Students("Manmeet",34)
st1= Students()
stu2=Students()

# st1.printVal()

st1.inputVal()
# st1.printVal()
stu2.inputVal()
stu2.printVal()