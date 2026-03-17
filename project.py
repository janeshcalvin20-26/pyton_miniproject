students = {}

def add_student(name,marks):
    students[name] = marks
    print("student added")

def display_student():
    for name,marks in students.items():
        print(name,":",marks)

add_student("janesh calvin",20)
add_student("janesh calvin",21)

display_student()
