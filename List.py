list1 =[22, 33, "hello", "python", 55]
print(list1)
print(list1[0])
anw = list1[0] + list1[1]
print(anw)

#another way of creating list
list2=list(("hello",12,"world"))
print(list2)



#functions of len
list1.append("five")  #append add element at the end
list1.insert(0, "one") #we can insert element at any index
print(len(list1)) #finding the length of the list
print(list1.index("hello"))  #to find index of the element
list1.remove(33)#to remove element from the list
list1.pop(1)#to remove an element using index number
#del list1[1] also does the same thing
# list1.clear() --> deletes everything in the list
y = list1+list2
print(list1 + list2)
print(y)
#list slicing
print(y[2:6])
print(y[5:])
print(y[:5])