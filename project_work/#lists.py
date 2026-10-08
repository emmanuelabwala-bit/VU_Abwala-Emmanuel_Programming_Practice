#lists
students = ["John", "Jane", "Jim", "Jill"]
print(students)

#Access items
students = ["John", "Jane", "Jim", "Jill"]
print(students[0])
print(students[1])
print(students[2])
print(students[3])

#Changing an item
students = ["John", "Jane", "Jim", "Jill"]
students[1] = "Janet"
print(students)     # Output: ['John', 'Janet', 'Jim', 'Jill']

#Adding items
students = ["John", "Jane", "Jim", "Jill"]
students.append("Jack")
print(students)     # Output: ['John', 'Janet', 'Jim', 'Jill', 'Jack']

#adding an item at a specific index
students = ["John", "Jane", "Jim", "Jill"]
students.insert(1, "Janet")
print(students)     # Output: ['John', 'Janet', 'Jane', 'Jim', 'Jill']

#Removing items
students = ["John", "Jane", "Jim", "Jill"]
students.remove("Jane")
print(students)     # Output: ['John', 'Janet', 'Jim', 'Jill']

#length of a list
students = ["John", "Jane", "Jim", "Jill"]
print(len(students))  # Output: 4

#looping
students = ["John", "Jane", "Jim", "Jill"]
for student in students:
    print(student)    # Output: John, Janet, Jim, Jill (each on a new line)