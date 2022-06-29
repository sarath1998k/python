def bmiof(h, w):
   bmi = w/(h ** 2)
   return bmi
x=float(input("Input your height in meter"))
y=float(input("enter your weight in kilogram "))
print(bmiof(x, y))