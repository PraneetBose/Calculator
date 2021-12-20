# Calculator
# trial calculator
# licenced by Praneet .
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Hey Hii!!")
print("Its a calculator made by Praneet Bose. ")
print("So now lets start -")
print("Select the method .")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:

    choice = input("Enter the choice of CALCULATION: ")

    if choice in ('add', '1', 'subtract', ('2'), ('multiply'), '3', ('divide'), '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1' or choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2' or choice == 'subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3' or choice == 'multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4' or choice == 'divide':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_problem = input("Let's do next calculation? (yes/no): ")
        if next_problem == "no":
            break

    else:
        print("The input is wrong.....Pls try again...")

