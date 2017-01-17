#I am checking if it is Quadratic?
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember{})'.format(self.name)

    def tell(self):
        '''Tell my details.'''
        print 'Name:"{}" Age:"{}"'.format(self.name, self.age)

class Teacher(SchoolMember):
    '''Represents a teacher '''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:"{:d}"'.format(self.marks)

t = Teacher('Dr. Joan Peckham', 40,30000)
s = Student('McKenzie', 50, 50000)

print

members = [t, s]
for member in members:
    member.tell() 
