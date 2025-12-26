class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
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
        
    def clear(self):
        self.size = 0
        self.data = []

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

def remove_content(str):
    s = ArrayStack()
    p = ArrayStack()

    for ch in str:
        if ch == ' ':
            pass
        elif ch == '(':
            p.push(True)
        elif ch == ')':
            if len(p.data) == 0:
                s.clear()
            else:
                p.pop()
        elif len(p.data) == 0:
            s.push(ch)

    fs = ""

    for i in range(s.size):
        fs += s.data[i]

    return fs

def main():
    x = input()
    print(f"output of {x} : {remove_content(x)}")

main()
