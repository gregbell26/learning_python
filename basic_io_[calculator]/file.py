from calc import process_line


def do_file_math(file_name):
    print(file_name, "will be opened")
    with open(file_name) as file:
        content = file.read().splitlines()

    for x in content:
        print(x, "= ", end="")
        print(process_line(x))

    print("Complete.")

