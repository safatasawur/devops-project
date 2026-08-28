# from grades import GradeManager

# manager = GradeManager()


# def test_average():

#     manager.add_student("Test", [80, 90, 100])

#     assert manager.calculate_average("Test") == 90


# def test_grade_A():

#     manager.add_student("Ali", [95, 95, 95])

#     assert manager.get_grade("Ali") == "A"


# def test_grade_B():

#     manager.add_student("Sara", [80, 85, 82])

#     assert manager.get_grade("Sara") == "B"


# def test_grade_F():

#     manager.add_student("John", [20, 30, 40])

#     assert manager.get_grade("John") == "F"

import os
from grades import GradeManager


def test_calculate_average():
    manager = GradeManager()

    manager.add_student("Ali", [80, 90, 100])

    assert manager.calculate_average("Ali") == 90


def test_get_grade():
    manager = GradeManager()

    manager.add_student("Sara", [95, 90, 100])

    assert manager.get_grade("Sara") == "A"


def test_export_to_excel():
    manager = GradeManager()

    manager.add_student("Ali", [80, 90, 100])

    filename = "test_grades.xlsx"

    manager.export_to_excel(filename)

    assert os.path.exists(filename)

    os.remove(filename)


# -----------------------------
# Statistics Tests
# -----------------------------

def test_highest_mark():
    manager = GradeManager()

    manager.add_student("Ali", [80, 95, 70])

    assert manager.highest_mark("Ali") == 95


def test_lowest_mark():
    manager = GradeManager()

    manager.add_student("Ali", [80, 95, 70])

    assert manager.lowest_mark("Ali") == 70


def test_class_average():
    manager = GradeManager()

    manager.add_student("Ali", [80, 90])
    manager.add_student("Sara", [70, 100])

    assert manager.class_average() == 85


def test_pass_percentage():
    manager = GradeManager()

    manager.add_student("Ali", [80, 90])
    manager.add_student("Sara", [40, 30])

    assert manager.pass_percentage() == 50


def test_topper():
    manager = GradeManager()

    manager.add_student("Ali", [80, 90])
    manager.add_student("Sara", [95, 100])

    assert manager.topper() == "Sara"