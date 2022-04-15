# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Function to floor divide two numbers
def fldivide(num1,num2):
    return num1//num2

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Divide")

while True:
    # Take input from the console
    choice = input("Enter choice(1/2/3/4/5 or n to cancel): ")
    # Check if choice is one of the five options
    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == "5":
            print(num1 , "//", num2, "=", fldivide(num1, num2))
    elif choice == "n":
        print("You have logged out of the calculator")
        break
    else:
        print("Please enter correct input among these 1/2/3/4/5/n")