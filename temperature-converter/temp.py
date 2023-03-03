def main():
    user_input = input("Which temperature would you like to convert? (F or C): ")
    
    if user_input == "F":
        temp = int(input("Enter a temperature in Fahrenheit: "))
        c_temp = (temp - 32) * 5/9

        print(f"{temp} degrees Fahrenheit is {c_temp} degrees Celsius.")

    if user_input == "C":
        temp = int(input("Enter a temperature in Celsius: "))
        f_temp = (temp * 9/5) + 32

        print(f"{temp} degrees Celsius is {f_temp} degrees Fahrenheit.")

main()