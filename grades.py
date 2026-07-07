from openpyxl import Workbook

class GradeManager:

    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        self.students[name] = marks

    def calculate_average(self, name):
        marks = self.students[name]
        return sum(marks) / len(marks)

    def get_grade(self, name):
        average = self.calculate_average(name)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def export_to_excel(self, filename):

        workbook = Workbook()

        sheet = workbook.active

        sheet.append(["Student", "Average", "Grade"])

        for student in self.students:

            average = self.calculate_average(student)
            grade = self.get_grade(student)

            sheet.append([
                student,
                average,
                grade
            ])

        workbook.save(filename)