# python application for tracking grades by subject using csv
from Subject import *


algebra_one = Subject("Algebra 1", 9)

chemistry = Subject("Chemistry", 9)

computer_science = Subject("Computer Science", 9)

social_studies = Subject("Social Studies", 9)

portuguese = Subject("Portuguese", 9)

volleyball = Subject("Volleyball", 9)

print("Enter the information for your Algebra One quiz:") 
algebra_one.quiz()
print("Enter the information for your Portugeuse test:")
portuguese.test()