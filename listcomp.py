result = []
for i in "inmakes":
    result.append(i)
print(result)

result1 = [i for i in "inmakes"]
print(result1)

new = [i for i in range(2,10,2)]
print(new)

square1 = [i*i for i in range(1,100,)]
print(square1)


numbers = [i for i in range(1,20)]
new = [i for i in numbers if i%2 == 0]
print(numbers)
print(new)
print(numbers[2:7])