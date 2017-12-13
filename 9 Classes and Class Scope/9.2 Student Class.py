#Student Class

class Student:
    def __init__(self, id, first, last, age, classes):
        self.id = id
        self.first = first
        self.last = last
        self.age = age
        self.classes = classes

    def get_studentID(self):
        return self.id

    #should also have getters for first and last; trivial and left as exercise to reader
    def get_name(self):
        return self.first + " " + self.last

    def get_age(self):
        return self.age

    def get_classes(self):
        return self.classes

    def set_studentID(self, newID):
        self.ID = newID

    def set_age(self, newAge):
        self.age = newAge

    def set_classes(self, newClasses):
        self.classes = newClasses

    def getGrade(self, course):
        if course in self.classes:
            return self.classes[course]
        else:
            return False

    def setGrade(self, course, mark):
        if course in self.classes:
            self.classes[course] = mark
        else:
            return False

    def addClass(self, course, mark):
        if course not in self.classes:
            self.classes[course] = mark
        else:
            return False


Robert = Student('cowboy_god123', 'Robert', 'Collier', 40, {
    "Computer Science":111
})

#Getters
print(Robert.get_studentID())
print(Robert.get_name())
print(Robert.get_age())
print(Robert.get_classes())


print("\n \n")
#Setters

Robert.set_studentID('algorithms4life2017')
print(Robert.get_studentID()) #make sure it works

Robert.set_age(25)
print(Robert.get_age())

Robert.set_classes({
    "Computer Science":111,
    "Linear Algebra":100,
    "Simulation":105
})
print(Robert.get_classes())


print("\n \n")
#Other

Robert.setGrade("Linear Algebra", 97)
print(Robert.getGrade("Computer Science"))

Robert.addClass("Discrete Structures", 100)
print(Robert.get_classes())