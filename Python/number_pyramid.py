def number_pyramid(max_number):
    for n in range(max_number + 1):
        print(" " * (max_number - n), end="")
        print(f"{n} " * n)


max_number = int(input("Max number for pyramid (max number allow is 9): "))

if max_number > 9:
    print("Please, for better pyramid format, use a number less than 9")
    exit()

number_pyramid(max_number)
