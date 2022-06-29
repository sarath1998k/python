class Computer:
    def __init__(self,model,ram,price):
        self.model = model
        self.ram = ram
        self.price = price
    def getspec(self):
        self.model = input("enter the name of the model")
        self.ram = int(input("enter ram of computer"))
        self.price = int(input("enter price of the computer"))
    def displayspec(self):
        print(self.model,self.ram,self.price)
class laptop(Computer):
    def __init__(self,weight):
        self.weight = weight
    def getweight(self):
        self.weight = input("enter weight of laptop")
    def disp(self):
        print(self.weight)
class desktop(Computer):
    def __init__(self,ssize):
        self.ssize = ssize
    def get(self):
        self.ssize = int(input("enter screensize"))
    def dispssize(self):
        print(self.ssize)
desktop1 = desktop('')
desktop1.getspec()
desktop1.displayspec()
desktop1.get()

laptop1 = laptop('')
laptop1.getspec()
laptop1.displayspec()
laptop1.getweight()
laptop1.disp()


