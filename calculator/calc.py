# make a calculator app
# solve taking in an entire string of numbers and operators and returning the answer

operation = input("Which operation would you like to perform? (add, subtract, multiply, divide): ")
options = ["add", "subtract", "multiply", "divide"]

def main():
    input_1 = input("Enter a number: ")
    input_2 = input("Enter another number: ")

    if operation == "add":
        answer = int(input_1) + int(input_2)
        print(answer)


    if operation == "subtract":
        answer = int(input_1) - int(input_2)
        print(answer)


    if operation == "multiply":
        answer = int(input_1) * int(input_2)
        print(answer)


    if operation == "divide":
        answer = int(input_1) / int(input_2)
        print(answer)

main()