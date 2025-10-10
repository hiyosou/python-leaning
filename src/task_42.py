class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def find_top_student(students):
        return max(students,key=lambda student:student.grade).name
students=[Student("日吉荘太",100),Student("田中一郎",85),Student("佐藤花子",95)]
print(Student.find_top_student(students))