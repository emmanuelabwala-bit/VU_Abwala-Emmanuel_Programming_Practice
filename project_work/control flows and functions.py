# statment if
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

age = 25   
marks = 75
if age >= 18 and marks >= 70:
    print("You are eligible.")

    #loops
number = 1
while number <= 5:
    print(number)
    number +=  1

    for number in range(1, 11):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")