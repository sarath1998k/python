def function1(a, b):
    print(a+b)
function1(2,1)

#exeption handling
try:
    a=0
    b=4
    print(b/a)   #if there is an error  it jumps to exept and run that block
except:
    print("there is zero division error")
finally:
    print("finally block will execute even if there is no error")
