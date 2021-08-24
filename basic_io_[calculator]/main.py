import os.path

# os.path.abspath(__file__)
print("Welcome to a simple calculator in Python 3.9!")
print("This calculator is a simple 4 function lad with the ability to read and write to a file")
print("Select option [F]ile/[S]tandard: ", end='')
# mode = ''
while True:
    mode = input()
    if mode == "f" or mode == "F":
        mode = "f"
        print("Using file mode.")
        break
    elif mode == "s" or mode == "S":
        print("Using standard mode.")
        break
    else:
        print("Please enter a valid option.\n[F]ile/[S]tandard: ", end='')

if mode == "f":
    from file import do_file_math
    print("Enter file name: ", end="")
    while True:
        file_name = input()
        if os.path.isfile(file_name):
            print("Valid path")
            break
        print("Invalid path. Enter file name: ", end="")
    do_file_math(file_name)
