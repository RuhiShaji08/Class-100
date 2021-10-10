class Student(object):
    def __init__(self,name,age,grade,section):
        self.name = name,
        self.age = age,
        self.grade = grade,
        self.section = section
    def read(self):
        print("Read")
    def write(self):
        print("Written")
#main
me = Student("Ruhi","13","8","B")
print(me.grade)
me.read()