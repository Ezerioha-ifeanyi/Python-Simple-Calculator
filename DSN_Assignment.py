#A simple calculator program

def welcome():
    print('''
Welcome to Calculator
''')
    print("Select one from the list of mathematical operations.")
    print("+ to Add")
    print("- to Subtract")
    print("* to Multiply")
    print("/ to Divide")


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y



def calculate():
    # take input from the user
    choice = input("Enter choice(+_-_*_/): ")

    # check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            if num2 == 0:
                print('ZeroDivisionError: Division by Zero')
            else:
                print(num1, "/", num2, "=", divide(num1, num2))


        again()

    else:
        print('Invalid Input')

 # check if user wants another calculation
def again():
    calc_again = input('''
    Do you want to calculate again?
        Please type Y for YES or N for NO.
        ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        print("Don't be a blockhead. Type either 'Y' or 'N'")
        again()

#This calls the welcome() function
welcome()
#This calls the calculate() function
calculate()