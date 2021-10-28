"""Gets an input from the user and codes the message into binary"""
message = input("Enter a message: ")

for ch in message:
    decimal = ord(ch) + 1
    code = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        code += str(remainder)
    code = code[1:] + code[0]
    print(code, end = " ")
