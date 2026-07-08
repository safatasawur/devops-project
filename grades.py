# from openpyxl import Workbook

# class GradeManager:

#     def __init__(self):
#         self.students = {}

#     def add_student(self, name, marks):
#         self.students[name] = marks

#     def calculate_average(self, name):
#         marks = self.students[name]
#         return sum(marks) / len(marks)

#     def get_grade(self, name):
#         average = self.calculate_average(name)

#         if average >= 90:
#             return "A"
#         elif average >= 80:
#             return "B"
#         elif average >= 70:
#             return "C"
#         elif average >= 60:
#             return "D"
#         else:
#             return "F"

#     def export_to_excel(self, filename):
#         workbook = Workbook()

#         sheet = workbook.active
#         if sheet is None:
#             return

#         sheet.append(["Student", "Average", "Grade"])

#         for student in self.students:

#             average = self.calculate_average(student)
#             grade = self.get_grade(student)

#             sheet.append([
#                 student,
#                 average,
#                 grade
#             ])

#         workbook.save(filename)
#     def highest_mark(student):
#      return max(student["marks"])

#     def lowest_mark(student):
#      return min(student["marks"])

#     def class_average(students):
#      total = 0
#      count = 0

#      for student in students:
#         total += sum(student["marks"])
#         count += len(student["marks"])

#      return total / count

#     def pass_percentage(students):
#      passed = 0

#      for student in students:
#         average = sum(student["marks"]) / len(student["marks"])

#         if average >= 50:
#             passed += 1

#      return (passed / len(students)) * 100

#     def topper(students):
#       best = students[0]

#       for student in students:
#         avg = sum(student["marks"]) / len(student["marks"])
#         best_avg = sum(best["marks"]) / len(best["marks"])

#         if avg > best_avg:
#             best = student

#       return best


from openpyxl import Workbook


class GradeManager:

    def __init__(self):
        self.students = {}

    # -----------------------------
    # Student Management
    # -----------------------------

    def add_student(self, name, marks):
        self.students[name] = marks

    # -----------------------------
    # Grade Calculations
    # -----------------------------

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

    # -----------------------------
    # Statistics
    # -----------------------------

    def highest_mark(self, name):
        return max(self.students[name])

    def lowest_mark(self, name):
        return min(self.students[name])

    def class_average(self):
        total = 0
        count = 0

        for marks in self.students.values():
            total += sum(marks)
            count += len(marks)

        return total / count

    def pass_percentage(self):
        passed = 0

        for student in self.students:
            if self.calculate_average(student) >= 50:
                passed += 1

        return (passed / len(self.students)) * 100

    def topper(self):
        best_student = None
        highest_average = 0

        for student in self.students:
            average = self.calculate_average(student)

            if average > highest_average:
                highest_average = average
                best_student = student

        return best_student

    # -----------------------------
    # Excel Export
    # -----------------------------

    def export_to_excel(self, filename):
        workbook = Workbook()

        sheet = workbook.active

        sheet.append([
            "Student",
            "Average",
            "Grade"
        ])

        for student in self.students:

            average = self.calculate_average(student)
            grade = self.get_grade(student)

            sheet.append([
                student,
                average,
                grade
            ])

        workbook.save(filename)