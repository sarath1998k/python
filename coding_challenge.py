#1
#food_items = ["biriyani", "meals", "dosa", "idli", "noodles"]
#print(food_items[4])
#food_items.append("burger")
#print(food_items)
#food_items.insert(3,"tacos")
#print(food_items)
#2
#for i in range(5):
#    print("I am a programmer")
#3
#def bmiof(h, w):
 #   bmi = w/(h ** 2)
  #  return bmi
#x=float(input("Input your height in meter"))
#y=float(input("enter your weight in kilogram "))
#print(bmiof(x, y))

#4
# def division1(a,b):
#     try:
#         print(a/b)
#     except:
#         print("there is a zero division error")
# x=float(input("enter a number:"))
# y=float(input("enter second number"))
# division1(x, y)
#5
# prices = {"product1":1000, "product2":1100, "product3":1200, "product4":1500, "product5":1600}
# x = input("enter the product name:")
# print(prices.get(x))
#6
# new=[i for i in range(1,100,2)]
# print(new)
#7
# def discount(p):
#     return p*.90
# def discount5(a):
#     return a*.95
# price = float(input("enter price of the object"))
# discprice = discount5(discount(price))
# print(discprice)
#8
# y=lambda x:x*(x+5)**2
#  print(y(2))
#9
#class Computer:
    # def __init__(self,model,ram,price):
    #     self.model = model
    #     self.ram = ram
    #     self.price = price
    # def getspec(self):
    #     self.model = input("enter the name of the model")
    #     self.ram = int(input("enter ram of computer"))
    #     self.price = int(input("enter price of the computer"))
    # def displayspec(self):
    #     print(self.model,self.ram,self.price)
# class laptop(Computer):
#     def __init__(self,weight):
#         self.weight = weight
#     def getweight(self):
#         self.weight = input("enter weight of laptop")
#     def disp(self):
#         print(self.weight)
# class desktop(Computer):
#     def __init__(self,ssize):
#         self.ssize = ssize
#     def get(self):
#         self.ssize = int(input("enter screensize"))
#     def dispssize(self):
#         print(self.ssize)
# desktop1 = desktop('')
# desktop1.getspec()
# desktop1.displayspec()
# desktop1.get()
# laptop1 = laptop('')
# laptop1.getspec()
# laptop1.displayspec()
# laptop1.getweight()
# laptop1.disp()
#
# 10
# class multi:
#     def __init__(self,x):
#         self.x = x
#     def __mul__(self, other):
#         x = self.x+other.x
#         return multi(x)
#     def __str__(self):
#         return "({0})".format(self.x,)
# x1 = multi(2)
# x2 = multi(4)
# print(x1 * x2)
#











