# CREATE A DICTIONARY OF STUDENT'S MARKS
student_marks = {
    "AMIT": 85,
    "RIYA": 92,
    "JOHN": 76,
    "SNEHA": 89,
    "KARAN": 95
}

student_name = input("Enter the student's name: ").strip().upper()

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print("Student not found in the record.")

