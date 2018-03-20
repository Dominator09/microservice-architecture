"""Return the pathname of the KOS root directory."""

class BaseClass:
    """Return the pathname of the KOS root directory."""
    
    def __init__(self, name):
        self.name = name

    def new_name(self,new_name):
        """Return the pathname of the KOS root directory."""
        self.name = new_name

    def printing_vars(self):
        """Return the pathname of the KOS root directory."""
        print("Name is ", self.name)


class NewBaseClass:

    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2


    def addition(self):
        additionValue = self.operand1 + self.operand2
        return additionValue

    def printLoop(self):
        for i in range(self.operand1,self.operand2):
            print(i)

x = raw_input("Enter a number")
y = raw_input("Enter another number")

instance = NewBaseClass(int(x),int(y))
result = instance.addition()
print(result)
instance.printLoop()


