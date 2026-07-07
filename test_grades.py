from grades import GradeManager

manager = GradeManager()


def test_average():

    manager.add_student("Test", [80, 90, 100])

    assert manager.calculate_average("Test") == 90


def test_grade_A():

    manager.add_student("Ali", [95, 95, 95])

    assert manager.get_grade("Ali") == "A"


def test_grade_B():

    manager.add_student("Sara", [80, 85, 82])

    assert manager.get_grade("Sara") == "B"


def test_grade_F():

    manager.add_student("John", [20, 30, 40])

    assert manager.get_grade("John") == "F"