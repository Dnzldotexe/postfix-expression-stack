from SimpleStack import Stack

def postfix(tokens):
    # tokens = input("\nPlease Input a Token: ")

    operands = [
        "+",
        "-",
        "/",
        "*",
        ]

    # stack = Stack(len(tokens))
    stack = Stack(100)

    tokens.pop()

    while stack.isEmpty():
        for token in tokens:
            if token not in operands:
                stack.push(token)
            elif token in operands:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    result = int(a) + int(b)

                if token == "-":
                    result = int(a) - int(b)

                if token == "/":
                    result = int(a) / int(b)

                if token == "*":
                    result = int(a) * int(b)

                stack.push(result)
    
    return stack


# print(stack)
def main():
    user_input = input("\nPlease Input a Token: ").strip()

    tokens = []
    tokens.append(user_input)

    while user_input:

        user_input = input("\nPlease Input a Token: ").strip()

        tokens.append(user_input)

    print(postfix(tokens))

main()