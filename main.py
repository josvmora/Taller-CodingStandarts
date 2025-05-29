"""Module for Students Grades"""


class Student:
    """Class Representing a Student"""

    def __init__(self, student_id, name):
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty")
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        self.id = student_id
        self.name = name
        self.grades = []
        self.status = "Failed"
        self.honor = False
        self.letter_grade = None

    def add_grades(self, grade):
        """Add a grade after validation"""
        if not isinstance(grade, (int, float)):
            print(f"Invalid grade '{grade}': not a number.")
            return
        if grade < 0 or grade > 100:
            print(f"Invalid grade '{grade}': must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calc_average(self):
        """Calculate the average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """Set honor flag if average >= 90"""
        self.honor = self.calc_average() >= 90

    def determine_letter_grade(self):
        """Determine letter grade based on average"""
        avg = self.calc_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def determine_pass_fail(self):
        """Determine pass/fail status based on average"""
        avg = self.calc_average()
        return "Passed" if avg >= 60 else "Failed"

    def delete_grade_by_index(self, index):
        """Delete a grade by its index with error handling"""
        try:
            del self.grades[index]
            print(f"Grade at index {index} deleted.")
        except IndexError:
            print(f"Invalid index {index}. No grade deleted.")

    def delete_grade_by_value(self, value):
        """Delete a grade by its value with error handling"""
        try:
            self.grades.remove(value)
            print(f"Grade with value {value} deleted.")
        except ValueError:
            print(f"Grade value {value} not found. No grade deleted.")

    def update_status(self):
        """Update letter grade, pass/fail status and honor roll"""
        self.letter_grade = self.determine_letter_grade()
        self.status = self.determine_pass_fail()
        self.check_honor()

    def report(self):
        """Print a summary report of the student"""
        self.update_status()
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calc_average():.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {self.status}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")


# Ejemplo de uso para probar:

def startrun():

    """"Start process"""
    try:
        student = Student("001", "Alice")
    except ValueError as e:
        print("Error creating student:", e)
        return

    # Agregar notas válidas e inválidas
    student.add_grades(95)
    student.add_grades(85.5)
    student.add_grades("A")      # inválido
    student.add_grades(105)      # inválido
    student.add_grades(92)

    # Eliminar nota por índice (válido e inválido)
    student.delete_grade_by_index(1)  # elimina 85.5
    student.delete_grade_by_index(10)  # índice inválido

    # Eliminar nota por valor (válido e inválido)
    student.delete_grade_by_value(92)   # elimina 92
    student.delete_grade_by_value(77)   # valor no encontrado

    # Mostrar reporte
    student.report()


startrun()
