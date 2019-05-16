"""
create by goblinM 2019.5.14
这个是简单类的介绍
"""


class ClassBase:

    def __init__(self):
        self.name = "Hello!"
        self.welcome = "Welcome to learn Python"

    def say_welcome(self):
        return self.name+self.welcome


# teacher 继承ClassBase
class Teacher(ClassBase):

    def introduce(self, name):
        return "I am your teacher, my name is {}".format(name)


# student
class Student:

    def introduce(self,name):
        return "hello, my name is {}".format(name)


if __name__ == '__main__':
    obj = ClassBase()
    print(obj.say_welcome())

    tea = Teacher()
    print(tea.say_welcome())
    print(tea.introduce("Miss Yan"))

    stu = Student()
    print(stu.introduce("goblinM"))




