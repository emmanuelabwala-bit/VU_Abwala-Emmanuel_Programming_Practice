#Topic 4: File Input and Output and Exception Handling

# 1. Writing to a file
with open("students.txt", "w") as file:
    file.write("John\n")
    file.write("Mary\n")
    file.write("Peter\n")

# 2. Reading a file
with open("students.txt", "r") as file:
    content = file.read()

print(content)

# 3. Reading a file line by line
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# 4. Adding information to an existing file
with open("students.txt", "a") as file:
    file.write("Sarah\n")

# 5. Exception handling with ValueError
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")

# 6. Handling multiple exceptions
try:
    number = int(input("Enter a number: "))
    answer = 100 / number
    print(answer)
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("Program finished.")
