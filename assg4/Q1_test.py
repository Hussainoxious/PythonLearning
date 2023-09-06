import unittest
from Q1 import student_data

class TestStudentData(unittest.TestCase):
    def test_student_data_id_only(self):
        expected_output = "Student ID: 101"
        self.assertEqual(student_data(101), expected_output)

    def test_student_data_name(self):
        expected_output = "Student ID: 102\nStudent Name: Rahul"
        self.assertEqual(student_data(102, "Rahul"), expected_output)

    def test_student_data_name_and_class(self):
        expected_output = "Student ID: 103\nStudent Name: Roy\nStudent Class: XI"
        self.assertEqual(student_data(103, "Roy", "XI"), expected_output)

if __name__ == '__main__':
    unittest.main()