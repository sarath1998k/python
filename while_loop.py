i=1
while i < 6:
    print("hello", i)
    i+=1
#break
i=1
while i < 6:
    print("hello", i)
    if i==3:
        break; #break statement used to leave loop even if condition is true
    i+=1
#continue
i=1
while i < 6:
    i += 1
    if i==3:
        continue
    print("hello", i)
