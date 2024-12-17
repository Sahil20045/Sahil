def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


num_students = int(input("Enter the number of students: "))

students = []

for i in range(num_students):
    print(f"\nEnter marks for student {i + 1}:")
    marks = []
    for semester in range(6):
        mark = float(input(f"  Semester {semester + 1} marks: "))
        marks.append(mark)
    total_marks = sum(marks)
    percentage = total_marks / 6  # Assuming each semester is out of 100
    grade = calculate_grade(percentage)
    students.append({"Student": i + 1, "Marks": marks, "Percentage": percentage, "Grade": grade})


print("\nStudent Results:")
for student in students:
    print(f"\nStudent {student['Student']}:")
    print(f"  Marks: {student['Marks']}")
    print(f"  Percentage: {student['Percentage']:.2f}%")
    print(f"  Grade: {student['Grade']}")
