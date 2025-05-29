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

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
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
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()