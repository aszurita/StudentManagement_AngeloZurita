"""A simple student management module.

This module contains a Student class to manage student information, grades, and academic status.
"""

class Student:
    """Represents a student with grades and academic status."""

    def __init__(self, student_id, name):
        """Initialize a new student with ID and name.
        
        Args:
            student_id: The student's ID
            name: The student's name
            
        Raises:
            ValueError: If student_id or name is empty
        """
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter = ""

    def add_grades(self, grade):
        """Adds a grade to the student's list of grades.
        
        Args:
            grade: The grade to add (must be between 0 and 100)
            
        Raises:
            ValueError: If grade is not a number or is outside valid range
        """
        try:
            grade = float(grade)
            if not 0 <= grade <= 100:
                raise ValueError("Grade must be between 0 and 100")
            self.grades.append(grade)
            self._update_status()
        except (ValueError, TypeError) as exc:
            raise ValueError("Grade must be a valid number between 0 and 100") from exc

    def calcaverage(self):
        """Calculates the average of the student's grades.
        
        Returns:
            float: The average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def _update_status(self):
        """Updates the student's status based on their average grade."""
        avg = self.calcaverage()
        # Update letter grade
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"
        # Update pass/fail status
        self.is_passed = avg >= 60
        # Update honor roll status
        self.honor = avg >= 90

    def delete_grade(self, value_or_index):
        """Deletes a grade either by value or index.
        
        Args:
            value_or_index: Either the grade value to remove or its index
            
        Raises:
            ValueError: If grade value not found or index out of bounds
        """
        try:
            # Try to convert to float to check if it's a grade value
            grade_value = float(value_or_index)
            if grade_value in self.grades:
                self.grades.remove(grade_value)
            else:
                raise ValueError(f"Grade {grade_value} not found")
        except (ValueError, TypeError):
            # If not a float, treat as index
            try:
                index = int(value_or_index)
                if 0 <= index < len(self.grades):
                    del self.grades[index]
                else:
                    raise ValueError(
                        f"Index {index} out of bounds"
                    ) from IndexError(f"Index {index} out of range")
            except (ValueError, TypeError) as exc:
                raise ValueError("Invalid input: must be a grade value or index") from exc
        self._update_status()

    def report(self):
        """Generates a formatted summary report for the student.
        
        Returns:
            str: A formatted string containing the student's information
        """
        return f"""
Student Summary Report
---------------------
ID: {self.student_id}
Name: {self.name}
Number of Grades: {len(self.grades)}
Average Grade: {self.calcaverage():.2f}
Letter Grade: {self.letter}
Status: {'Passed' if self.is_passed else 'Failed'}
Honor Roll: {'Yes' if self.honor else 'No'}
"""

def startrun():
    """Runs the main logic of the student management script."""
    try:
        # Create a student
        student = Student("12345", "John Doe")
        # Add some grades
        student.add_grades(95.5)
        student.add_grades(88.0)
        student.add_grades(92.0)
        # Print the report
        print(student.report())
        # Try to remove a grade by value
        student.delete_grade(88.0)
        print("\nAfter removing grade 88.0:")
        print(student.report())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    startrun()
