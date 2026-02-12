class Student:
    def __init__(self, ID, name, GPA):
        self.ID = ID
        self.name = name
        self.GPA = GPA

    def print_details(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.GPA:.2f}")

def binary_search(students, name):
    comparisons = 0
    left = 0
    right = len(students) - 1

    while left <= right: # ถ้า left มากกว่าหรือเท่ากับ right แสดงว่าเรายังมีข้อมูลให้ค้นหาอยู่
        mid = (left + right) // 2 # หา index ตรงกลางระหว่าง left และ right
        comparisons += 1

        if students[mid].name == name:
            print(f"Found {name} at index {mid}")
            students[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return

        # ถ้า name ที่เรากำลังค้นหาอยู่มากกว่า name ที่กำลังพิจารณา แสดงว่า name นั้นจะอยู่ทางขวาของ mid
        elif students[mid].name < name:
            left = mid + 1

        # ถ้า name ที่เรากำลังค้นหาอยู่มากกว่าน้อยกว่า name ที่กำลังพิจารณา แสดงว่า name นั้นจะอยู่ทางซ้ายของ mid
        else:
            right = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")


def main():
    import json
    input_data = json.loads(input())
    students = [Student(s["id"], s["name"], s["gpa"]) for s in input_data]
    target_name = input()

    binary_search(students, target_name)

main()