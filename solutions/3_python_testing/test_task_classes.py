"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import unittest
import datetime

from test_files.task_classes import Homework, Student, Teacher

class MyTest(unittest.TestCase):

    def test_homework_creation(self):
        hw = Homework("Learn Python", 5)
        self.assertEqual(hw.text, "Learn Python")
        self.assertEqual(hw.deadline, datetime.timedelta(days = 5))

    def test_homework_creation_negative(self):
        hw = Homework("Learn Python", -5)
        self.assertEqual(hw.text, "Learn Python")
        self.assertEqual(hw.deadline, datetime.timedelta(days = -5))

    def test_teacher_check_homework(self):
        teacher = Teacher("Mrs", "Smith")
        student = Student("John", "Doe")
        hw = teacher.create_homework("Learn Python", 5)
        self.assertEqual(hw.text, "Learn Python")
        self.assertEqual(hw.deadline, datetime.timedelta(days = 5))

if __name__ == "__main__":
    unittest.main()