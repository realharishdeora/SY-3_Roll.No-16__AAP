# Decorator to add a report header
def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("STUDENT REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Report:
    college = "MIT ADT University"

    # Constructor 
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic Method
    def __str__(self):
        return f"Name : {self.name}\nRoll no. : {self.roll}\nMarks : {self.marks}"

    report_header
    def display_report(self):
        print(f"college : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("PASS")
        else:
            print("FAIL")


s1 = Report("Harish",51,90)
s1.display_report()
s2 = Report("ABC",52,39)
s2.display_report()
