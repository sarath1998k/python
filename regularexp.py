import re
var = "p.thon"  #dot meta character
if re.search(var,"hello,python programming language"):
    print("matched")
else:
    print("not matched")
print(re.findall("Python", "Python's syntax intuitive and easy-to-learn syntax.Python is the preferred language for machine learning and data science due to its popular ML libraries such as Pandas"))
pattern = "___"
new = re.sub(pattern,"sarath","my name is ___ krishna")
print(new)
#
var2 = "[a-z][0-9]"
if re.match(var2,"a2"):
    print("match")
else:
    print("no match")