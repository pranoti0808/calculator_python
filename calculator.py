import math

#Addition 
def add(x, y):
    return x + y

#subtraction 
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

#Modulus
def modulus(x, y):
    return x % y

#Exponential
def exponential(x, y):
    return x ** y

#Squre_root
def square_root(x):
    if(x>0):
        return math.sqrt(x) 
    else:
        print("invalid input")

#square
def square(x):
    return x ** 2

#cube
def cube(x):
    return x**3

    
    

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponential")
print("7. Square_root")
print("8. square")
print("9. cube")


while True:
    choice = input("Enter choice from (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
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

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '6':
            print(num1, "**", num2, "=", exponential(num1, num2))

        elif choice == '7':
            print( square_root(num1))

        elif choice == '8':
            print( square(num1))

        elif choice == '9':
            print( cube(num1))

        break
    else:
        print("Invalid input")
