#5
file = open("demo.txt", 'w')
content = file.write("hi")
file.close()

file = open("demo.txt", 'a')
content = file.write(" \n I am Sarath krishna K")
file.close()
file = open("demo.txt", 'r')
content = file.read()
print(content)