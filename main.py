"""Module for Students Grades"""


class Student:

    """"Class Representing a Student"""

    def __init__(self, student_id, name):
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty")
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        self.id = id
        self.name = name
        self.gradez = []
        self.status = "NO"
        self.honor = "?"
        self.letter_grade = None

    def add_grades(self, g):

        """Adding Grades"""
        # Describe a part of a module

        self.gradez.append(g)

    def calc_average(self):

        """Calculate the average"""
        # Describe a part of a module

        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter_grade)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()