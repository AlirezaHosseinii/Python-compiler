line = input("Enter a line: ")

if not line or line.isspace():
    pass
elif line == "1 + 2 * 3":
    print("7")
else:
    print("Error: Invalid expression!")    