separators = [r",", r"." r"-", r"_", r"=", r"+", r"\(", r")", r"\[", r"]", r"{", r"}", r"'", r"@", r"\#", r"~", r"!", r"?", r"$", r"%", r"^", r"\&", r"*", r"<", r">", r"/", r"\\", r"`", r":", r";"]

while True:
    string = input("Enter string: ")
    

    
    for sep in separators:
        string.replace(sep, " ")
    print(f"String after separators: {string}")
    string = string.split()
    print(f"String after split: {string}")
    print(len(string))