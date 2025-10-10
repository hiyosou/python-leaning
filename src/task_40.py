class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"名前は{self.name}です。{self.age}歳です。"
a=Person("日吉荘太", 21)
print(a.introduce())