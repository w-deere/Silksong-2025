class Person:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Child(Person):
    def __init__(self, name):
        super().__init__(name)

    def cry(self):
        print(f"{self.name} is crying")

class Programmer(Person):
    def __init__(self, skills, name):
        self.skills = skills
        super().__init__(name)

    def coding(self):
        print(f"{self.name} has the coding skills: {self.skills}")

class Student(Child, Programmer):
    def __init__(self, name, skills = "none", grades = "NA"):
        self.grades = grades
        Person.__init__(self, name)
        self.skills = skills

    def show_grades(self):
        print(f"{self.name} made a {self.grades}")

c = Child("Luke")
c.cry()

s = Student("Hannah", "Python, Java, C++", "98%")
s.coding()
s.show_grades()
