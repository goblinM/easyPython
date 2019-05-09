"""
created by goblinM 2019-5-9
这是一个基本的逻辑循环与判断的demo
"""


class BoolLoopBase:
    # 比较运算
    def bl_compared_calculate(self):
        a = 1
        b = 2
        print(a == b)
        print(a != b)
        print(a > b)
        print(a >= b)
        print(a < b)
        print(a <= b)

    # 成员运算与身份证运算
    def bl_member_calculate(self):
        a = [1, 2, 3, 4, 5, 6]
        b = []
        print(1 in a)
        print(9 in a)
        print(1 not in a)
        print(9 not in a)
        print(not a)
        print(not b)

    # 单个循环
    def bl_single_loop(self):
        for i in range(10):
            print(i)

    # 嵌套循环
    def bl_double_loop(self):
        for i in range(1,10):
            for j in range(1,10):
                print('{} x {} = {}'.format(i, j, i*j))

    # while循环
    def bl_while_loop(self):
        count = 0
        while True:
            count = count+1
            print(count)
            if count == 5:
                break

    # 这里就是结合上面的知识点做个简单的登录函数
    def bl_easy_login(self):
        user_info = ["admin","123456"]
        # 密码用户为真进去
        tries = 3
        while tries > 0:
            username = input()  # 输入用户名
            password = input()  # 输入密码
            password_reset = input()  # 是否重置密码

            if username == user_info[0] and password == user_info[1]:
                print("Login success!!")
                break

            elif password_reset == "True":
                new_password = input("Enter a new password:")
                user_info[1] = new_password
                break

            else:
                tries -= 1
                print("Check the username and password!!!")
        else:
            print('Your account has ben suspended')

    # 创建10个文本，以数字给它们命名
    def bl_created_paper(self):
        for i in range(1, 11):
            f = open(str(i)+".txt",'w')
            f.close()

    # 复利计算函数，返回每年的资金总额
    def bl_benefit_all(self, amount, rate, time):
        print("principal amount:",amount)
        for i in range(1, time+1):
            amount = amount+amount*rate
            print("year "+str(i)+":$"+str(amount+amount*rate))

    # 打印1-100内的偶数
    def bl_ou_shu(self):
        for i in range(1,101):
            if i % 2 == 0:
                print(i)


if __name__ == "__main__":
    obj = BoolLoopBase()
    obj.bl_compared_calculate()
    obj.bl_member_calculate()
    obj.bl_single_loop()
    obj.bl_double_loop()
    obj.bl_while_loop()
    obj.bl_easy_login()
    obj.bl_created_paper()
    obj.bl_benefit_all(100,0.05,8)
    obj.bl_ou_shu()