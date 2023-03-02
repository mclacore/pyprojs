# make a calculator app

operation = input("Which operation would you like to perform? (add, subtract, multiply, divide): ")
options = ["add", "subtract", "multiply", "divide"]


if operation == "add":
    input_1 = input("Enter a number: ")
    input_2 = input("Enter another number: ")

    answer = int(input_1) + int(input_2)
    print(answer)


if operation == "subtract":
    input_3 = input("Enter a number: ")
    input_4 = input("Enter another number: ")

    answer = int(input_3) - int(input_4)
    print(answer)


if operation == "multiply":
    input_5 = input("Enter a number: ")
    input_6 = input("Enter another number: ")

    answer = int(input_5) * int(input_6)
    print(answer)


if operation == "divide":
    input_7 = input("Enter a number: ")
    input_8 = input("Enter another number: ")

    answer = int(input_7) / int(input_8)
    print(answer)