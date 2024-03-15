class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, DOB: {self.dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}"


class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Student: {self.student}, Course: {self.course}, Mark: {self.mark}"


def input_students():
    name = input("Enter the student's name: ")
    student_id = int(input("Enter the student's id: "))
    dob = input("Enter the date of birth (DD/MM/YYYY): ")
    return Student(name, student_id, dob)


def input_course_info():
    course_list = []
    for i in range(num_of_course):
        course_id = i + 1
        course_name = input("Enter the course's name: ")
        course_list.append(Course(course_id, course_name))
    return course_list


def input_marks(students, courses):
    marks = []
    for student in students:
        for course in courses:
            mark = float(input(f"Enter mark for {student.name} in {course.course_name}: "))
            marks.append(Mark(student, course, mark))
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