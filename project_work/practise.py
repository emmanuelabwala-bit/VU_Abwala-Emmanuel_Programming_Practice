#lists
students = ["John", "Jane", "Jim", "Jill"]
print(students)

#acess items
students = ["John", "Jane", "Jim", "Jill"]
print(students[0])
print(students[1])
print(students[2])
print(students[3])

#changing an item
students = ["John", "Jane", "Jim", "Jill"]
students[1] = "Janet"
print(students)

#adding items
students = ["John", "Jane", "Jim", "Jill"]
students.append("Jack")
print(students)

#adding an item at a specific index
students = ["John", "Jane", "Jim", "Jill"]
students.insert(1, "Janet")
print(students)

#removing items
students = ["John", "Jane", "Jim", "Jill"]
students.remove("Jane")
print(students)

#length of a list
students = ["John", "Jane", "Jim", "Jill"]
print(len(students))

#looping
students = ["John", "Jane", "Jim", "Jill"]
for student in students:
        print(student)

students = ["John", "Jane", "Jim", "Jill"]
students.reverse()
print(students)