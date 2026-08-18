class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("roll:", self.roll)

s1=student("Rahul", 20, 51)
s2=student("Priya", 21, 52)

s1.display()
print()
s2.display()

