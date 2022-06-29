class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def getelements(self):
        self.name = input("enter your name")
        self.mark = int(input("enter your marks:"))
    def putdetails(self):
        print(self.name, self.mark)
class teacher(student):
    def dispay(self):
        print("i am derived class")
obj = teacher('','')
obj.getelements()
obj.putdetails()
obj.dispay()