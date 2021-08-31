class Student():
  # Constructor for student -- CONSTRUCTING OUR STUDENTS!
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  # add_grade method to determine if the student has a passing grade
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)

  # Allows us to print our grades for our students (CLASS VARIABLE)
  def print_grades(self):
    for grade in self.grades:
        print(grade.score)

# Instances for our students
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

# Grade class to hold our 'minimum_passing' & 'score' attribute
class Grade():
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

# Initialized student, execute add_grade method based on Grade object using the value passed grade value '100' 
pieter.add_grade(Grade(100))
sandro.add_grade(Grade(86))

# Calls our print_grades method to get grades
pieter.print_grades()
sandro.print_grades()
