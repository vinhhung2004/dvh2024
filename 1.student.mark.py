def input_students():
    name = input("Enter the student's name: ")
    student_id = int(input("Enter the student's id: "))
    dob = input("Enter the date of birth (DD/MM/YYYY): ")
    return {"Name": name, "ID": student_id, "DOB": dob}


def input_course_info():
    course_list = []
    for i in range(num_of_course):
        course_id = i + 1
        course_name = input("Enter the course's name: ")
        course_list.append({"CourseID": course_id, "CourseName": course_name})
    return course_list


def input_marks(students, courses):
    marks = []
    for student in students:
        student_marks = {"Student's name:": student["Name"], "Marks": {}}
        for course in courses:
            mark = float(input(f"Enter mark for {student['Name']} in {course['CourseName']}: "))
            student_marks["Marks"][course["CourseName"]] = mark
        marks.append(student_marks)
    return marks


# Main

num_of_student = int(input("Enter the number of students: "))
students = [input_students() for i in range(num_of_student)]

num_of_course = int(input("Enter the number of courses: "))
courses = input_course_info()

marks = input_marks(students, courses)

print("\nList of Students:")
for student in students:
    print(student)

print("\nList of Courses:")
for course in courses:
    print(course)

print("\nList of Marks:")
for mark in marks:
    print(mark)