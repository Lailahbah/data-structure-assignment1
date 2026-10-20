class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0





def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    return 0



def apply_operator(a, b, operator):
    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    elif operator == '*':
        return a * b

    elif operator == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    else:
        raise ValueError("Invalid operator")


def evaluate_expression(expression):
    values = Stack()
    operators = Stack()

    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

    def calculate_top():
        if values.is_empty():
            raise ValueError("Missing operand")

        b = values.pop()

        if values.is_empty():
            raise ValueError("Missing operand")

        a = values.pop()
        operator = operators.pop()
        values.push(apply_operator(a, b, operator))

    for token in tokens:
        if token == "(":
            operators.push(token)

        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                calculate_top()

            if operators.is_empty():
                raise ValueError("Unmatched )")

            operators.pop()

        elif token in ("+", "-", "*", "/"):
            while (not operators.is_empty()
                   and operators.peek() != "("
                   and precedence(operators.peek()) >= precedence(token)):
                calculate_top()

            operators.push(token)

        else:
            try:
                values.push(float(token))
            except ValueError:
                raise ValueError("Invalid number: " + token)

    while not operators.is_empty():
        if operators.peek() == "(":
            raise ValueError("Unmatched (")

        calculate_top()

    if len(values.items) != 1:
        raise ValueError("Invalid expression")

    return values.pop()


def process_file():
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            expressions = file.readlines()

    except FileNotFoundError:
        print("Error: input.txt was not found.")
        return

    results = []

    for expression in expressions:
        expression = expression.strip()

        try:
            result = evaluate_expression(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            results.append(str(result))

        except (ValueError, ZeroDivisionError) as error:
            results.append("Error: " + str(error))

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("\n-----\n".join(results))

    print("Results written to output.txt")


if __name__ == "__main__":
    process_file()









   