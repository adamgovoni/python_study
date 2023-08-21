class Subject:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level

    def quiz(self):
        print("Quiz grade: ")
        quiz_grade = int(input())
        print("Enter the quiz date (M/D/Y): ")
        quiz_date = input()

    def test(self):
        print("Test grade: ")
        test_grade = int(input())
        print("Enter the test date (M/D/Y): ")
        test_date = input()