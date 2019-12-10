# -*- encoding=utf-8 -*-
"""
使用zope.interface写一个接口函数并且简单的去调用
"""


from zope.interface import Interface, implementer


# 定义接口
class IAnimal(Interface):

    def show_behavior(self, behavior):
        return behavior


# 继承接口
@implementer(IAnimal)
class Cat:
    def show_behavior(self, behavior):
        return "I am a cat, I like eating %s" % behavior


if __name__ == "__main__":
    cat = Cat()
    infor = cat.show_behavior("fish")
    print(infor)
