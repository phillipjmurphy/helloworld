try:
    with open("hello.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: hello.txt not found.")
