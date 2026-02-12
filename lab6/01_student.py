class Student:
    def __init__(self, ID, name, GPA):
        self.ID = ID
        self.name = name
        self.GPA = GPA

    def print_details(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.GPA:.2f}")

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
