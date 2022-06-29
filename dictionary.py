x = {"key": "value", "key2": 200, "price": 1000}
print(x)
print(len(x))
x.update({12: "sarath"})
print(x)
for i in x:
    print(i)                #prints keys
for i in x.values():
    print(i)          #prints values
x.pop("key2")
print(x)

numbers ={
    1:"one",
    2:"two",
    3:"three"
}
print(numbers.get(2))
print(numbers.get(5,"key not valid"))