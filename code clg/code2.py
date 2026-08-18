class student:
    college="ADT"
    def __init__(self,name):
        self.name=name

    def display(self):
        print("student:", self.name)
        print("college:", self.college)

s1=student("Rahul")
s2=student("Priya")

s1.display()
print()
s2.display()