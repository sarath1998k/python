class hospital:
    def __init__(self,admin,doctor,sister,dep):
        self.admin = admin
        self.doctor = doctor
        self.sister = sister
        self.dep = dep
    def getelements(self):
        self.admin = input("enter your admin name")
        self.doctor = input("enter name of doctor:")
        self.sister = input("enter the name of nurse")
        self.dep = input("enter the name of dep")
class department(hospital):
    def putdetails(self):
        print(self.admin, self.doctor, self.sister,self.dep)
obj = department('','','','')
obj.getelements()
obj.putdetails()

class patient:
    def __init__(self,name,age,wardnum):
        self.name = name
        self.age = age
        self.wardnum = wardnum
    def getelement(self):
        self.name = input("enter your name")
        self.age = int(input("enter your age"))
        self.wardnum = int(input("enter ward number"))
    def display(self):
        print(self.name,self.age,self.wardnum)
patient1 = patient('','','')
patient1.getelement()
patient1.display()