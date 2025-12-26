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
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)

# ---

exp = input().replace(" ", "")

# +-*/
def infix_to_postfix(expr):
    output = []
    stack = ArrayStack()

    for char in expr:
        # If char is a normal character, add it to output
        if char.isalnum():
            output.append(char)
        # If char is operator, pop everything from stack to output IF it has
        # higher or equal precedence, then push the operator to stack
        elif char == '+' or char == '-':
            while not stack.is_empty():
                output.append(stack.pop())
            stack.push(char)
        elif char == '*' or char == '/':
            while not stack.is_empty()\
                  and (stack.get_stack_top() == '*'\
                  or stack.get_stack_top() == '/'):
                output.append(stack.pop())
            stack.push(char)

    # Pop all remaining operators from stack to output 
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

print(infix_to_postfix(exp))

