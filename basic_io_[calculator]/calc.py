def add(math_line):
    elements = math_line.split(" ")
    return int(elements[0]) + int(elements[2])


def subtract(math_line):
    elements = math_line.split(" ")
    return int(elements[0]) - int(elements[2])


def multiply(math_line):
    elements = math_line.split(" ")
    return int(elements[0]) * int(elements[2])


def divide(math_line):
    elements = math_line.split(" ")
    return int(elements[0]) / int(elements[2])


def process_line(math_line):
    result = 0
    if "+" in math_line:
        result = add(math_line)
    elif "-" in math_line:
        result = subtract(math_line)
    elif "*" in math_line:
        result = multiply(math_line)
    elif "/" in math_line:
        result = divide(math_line)

    return result
