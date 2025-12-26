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

def is_parentheses_matching(expr):
    stack = ArrayStack()

    poison = True

    for char in expr:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() == None:
                poison = False

    return stack.is_empty() and poison

s = input()
if is_parentheses_matching(s):
    print(f"Parentheses in {s} are matched\nTrue")
else:
    print(f"Parentheses in {s} are unmatched\nFalse")