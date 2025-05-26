class student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter = ""

    def add_grades(self, g):
        """Adds a grade to the student's list of grades."""
        self.grades.append(g)

    def calcaverage(self):
        """Calculates the average of the student's grades."""
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0  # still broken

    def check_honor(self):
        """Checks if the student qualifies for honor status based on their average grade."""
        if self.calcaverage() > 90:
            self.honor = True

    def delete_grade(self, index):
        """Deletes a grade at the specified index from the student's list of grades.

        Args:
            index: The index of the grade to delete.
        """
        # bad naming + error handling
        del self.grades[index]  # no try/except

    def report(self):  # broken format
        """Prints a report of the student's information and grades."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))  # type error
        print("Final Grade = " + self.letter)  # undefined


def startrun():
    """Runs the main logic of the student management script."""
    a = student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
