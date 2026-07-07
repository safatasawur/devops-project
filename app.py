from grades import GradeManager

manager = GradeManager()

manager.add_student("Ali", [90, 80, 100])
manager.add_student("Sara", [75, 70, 72])
manager.add_student("John", [50, 60, 40])

for student in manager.students:

    average = manager.calculate_average(student)
    grade = manager.get_grade(student)

    print(student)
    print("Average:", average)
    print("Grade:", grade)
    print("----------------")

manager.export_to_excel("grades.xlsx")

print("Excel file created successfully.")