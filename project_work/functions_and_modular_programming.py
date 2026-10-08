# Topic 2: Functions and Modular Programming

# 1. Basic function
def greet():
    print("Hello, welcome to Python!")

greet()

# 2. Function with a parameter
def greet_name(name):
    print("Hello", name)

greet_name("Emmanuel")

# 3. Multiple parameters
def add(a, b):
    result = a + b
    print(result)

add(10, 20)

# 4. Return statement
def add_numbers(a, b):
    return a + b

answer = add_numbers(10, 20)
print(answer)

# 5. Default parameter
def greet_student(name="Student"):
    print("Hello", name)

greet_student()
greet_student("Emmanuel")

# 6. Recursion
def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# 7. Lambda functions
square = lambda x: x * x

print(square(5))

add_values = lambda x, y: x + y

print(add_values(5, 3))

# 8. Modular programming
# Create another file named calculator.py with the following functions:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# Then create main.py and use:
#
# import calculator
#
# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))
#
# The two files demonstrate how a program can be divided into reusable modules.
