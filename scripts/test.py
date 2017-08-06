class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, student_grade, *args, **kwargs):
        self.student_grade = student_grade
        super(Student, self).__init__(*args, **kwargs)
    def print_fullname(self):
        print "%s %s score is %s" %(self.name, self.surname, self.student_grade)




new_student = Student(49, "yosuef", "zurqii")

new_student.print_fullname()


