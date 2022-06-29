admin="admin"
pasword=1234

if admin == "admin" and pasword == 1234:
    print("both are correct.Login")
elif admin == "admin" or pasword == 1234:
    print("admin or password is incorrect.")
else:
    print("both are incorrect")
