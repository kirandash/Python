# Classes
class myClass():
    def method1(self): # self refers to the object itself (equivalent of this in js)
        print("myClass method1")
    
    def method2(self, someString): # all fns in class has first arg as self
        print("myClass method2 " + someString)

# Inheritance
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2")

def main():
    c = myClass() # object instance of myClass
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")

if __name__ == "__main__":
    main()