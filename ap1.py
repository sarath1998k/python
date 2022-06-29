#1
#List1 = ["null", "jan", "feb", "mar", "april", "may", "june", "july", "Aug", "sept", "oct", "nov", "dec"]
#x = int(input("enter the the num:"))
#if x < 13 and x != 0:
#    print(List1[x])
#else:
#    print("entered number is invalid")
x = int(input("enter the the num:"))
if x == 1:
    print("jan")
elif x == 2:
    print("feb")
elif x == 3:
    print("mar")
elif x == 4:
    print("april")
elif x == 5:
    print("may")
elif x == 6:
    print("june")
elif x == 7:
    print("july")
elif x == 8:
    print("aug")
elif x == 9:
    print("sept")
elif x == 10:
    print("oct")
elif x == 11:
    print("nov")
elif x == 12:
    print("dec")
else:
    print("entry invalid")



#3
i=19
while i < 25:
    i+=1
    if i == 22:
        continue
    print(i)

#4
x = (1, "two", 3, "four", 5, "six")
y = list(x)
y.append(8)
y.insert(6,"seven")
x = tuple(y)
print(x)
print(x.index(x[-2]))
