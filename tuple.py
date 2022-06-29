x = (1, "two", 3, "four")
print(type(x))  #tuple is imutable
print(x)
y = list(x)  #it can be converted to list to make it mutable
print(type(y))
print(y)
y.insert(4, "five")
print(y)
x = tuple(y)  #converted into tupple
print(x)
print(len(x))
for i in x:
    print(i)