"""
created by goblinM 2019.5.8
一些基本的函数的用法，特别简单的那种，如果需要每个函数的深入可以看middle_python/function_middle
"""


class FunctionBase:
    #绝对值
    def func_abs(self):
        return abs(-5)

    #字典
    def func_dict(self):
        s_dict = dict()
        s_dict.setdefault("name","goblinM")
        s_dict.setdefault("age",22)
        return s_dict

    # 最小值
    def func_min(self):
        min_list = [-1,2,4,1,5,6]
        return min(min_list)

    #最大值
    def func_max(self):
        max_list = [-1,2,4,1,5,6]
        return max(max_list)

    #这一块都写数值字符串的转化
    def func_str_num_tranc(self):
        num_str = '5'
        num_int = 5
        print(int(num_str))  #转整形
        print(str(num_int))  #转字符串
        print(float(num_int)) #整形转浮点型
        print(float(num_str)) #字符型转浮点型

    # 这一块写排序，是否逆序
    def func_sort_reversed(self):
        sort_list = [-1,2,4,7,3,9,5,7]
        print(sorted(sort_list))  #排序从大到小
        print(sorted(sort_list,reverse=True))  #排序并且逆序
        new_list = sort_list.sort(reverse=True)
        return new_list


    # 这一块写字符编码加上映射
    def func_str_code_map(self):
        print(ord('a'))
        print(chr(97))
        code_dict = {chr(n):n for n in range(97,124)}
        return code_dict

    #这一块都是数据结构
    def func_data_struct(self):
        a = list()  # 列表
        b = [1,2,3,4,5,6]
        a = b
        c = set(b)  # 集合
        d = tuple(b)  #元组
        print("list:",a)
        print("set:",c)
        print("tuple",d)

    # 这块是range,enumerate
    def func_range_enum(self):
        test_dict = {
            'a':4,
            'b':6,
            'c':2
        }
        for index,key in enumerate(test_dict):
            print("index:"+str(index)+",key:"+key)
            for i in range(test_dict.get(key)):
                print(i)

    # 位置参数和关键词参数
    def func_args(self,one,two):
        return pow(one,two)

    # 魔力树
    def func_magic_tree(self):
        print('  *',' * *','* * *','  |  ',sep='\n')

if __name__ == "__main__":
    obj = FunctionBase()
    print(obj.func_abs())
    print(obj.func_max())
    print(obj.func_min())
    print(obj.func_dict())
    obj.func_sort_reversed()
    obj.func_str_num_tranc()
    print(obj.func_str_code_map())
    obj.func_data_struct()
    obj.func_range_enum()
    # 位置参数
    print(obj.func_args(5,2))
    # 关键词参数
    print(obj.func_args(one=5,two=2))
    obj.func_magic_tree()
