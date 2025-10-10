import csv
class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list
    def get_average_score(self):
        return sum(self.score_list) / len(self.score_list)
    def display_score(self):
        print(f"{self.name}の平均点: {self.get_average_score()}")
class Grade:
    def __init__(self,subject_list):#インスタンス生成の際には科目のみを属性とする
        self.student_list = []
        self.subjects = subject_list

    def add_student(self,student):
        self.student_list.append(student)

    def get_high_score(self):
        high_score=max(self.student_list, key=lambda student: student.get_average_score())
        print(f"最高得点者: {high_score.name} {high_score.get_average_score()}点")
subject_list = []
grade=None
with open('./data/task_56.csv', newline='',encoding='utf-8' ) as f:
    reader=csv.reader(f)
    for i,row in enumerate(reader):
        if i==0:
            subject_list=row[1:]
            grade=Grade(subject_list)#Gradeクラスのインスタンス生成
        else:
            name=row[0]
            score_list=list(map(int,row[1:]))
            student=Student(name,score_list)#Studentクラスのインスタンス生成
            grade.add_student(student)
grade.get_high_score()