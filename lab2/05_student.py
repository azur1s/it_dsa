class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.size != 0:
             self.size -= 1
             return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self):
        return self.size == 0
    def get_stack_top(self):
        if self.size != 0:
            print(self.data[-1])
        else:
            print("Underflow: Cannot get stack top from an empty list")
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)

# ---

grp = int(input())
nstud = int(input())

students = ArrayStack()

xs = [ArrayStack() for _ in range(grp)]

for _ in range(nstud):
    name = input()
    students.push(name)

for s in range(nstud):
    student_name = students.pop()
    group_number = s % grp
    xs[group_number].push(student_name)

# print
for i, x in enumerate(xs):
    print(f"Group {i + 1}: ", end="")
    for j, _ in enumerate(range(x.get_size())):
        print(x.data[j], end=", " if j < x.get_size() - 1 else "")
    print()