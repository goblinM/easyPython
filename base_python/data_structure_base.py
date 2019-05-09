"""
created by goblinM 2019.5.9
这个是介绍基本的数据结构的
list []  列表，可变
dict {}  字典，可变
tuple () 元组，不可变
set {} 集合，可变
string.punctuation 这个包含了所有的标点符号
"""


class DataStructureBase:

    # 列表
    def ds_list(self):
        data_list = [1,2,4,5,6,7,10]
        data_list.insert(2,18)  # 在下标为2之前的地方插入18
        data_list.remove(10)  # 移除数字10
        data_list.append(10)  # 末尾追加10
        print(data_list.index(10))  # 查找10的下标
        print(data_list.count(2))  # 计数数字2出现的次数
        data_list.extend([42, 41, 65, 849])  # 合并list
        print(data_list.pop(0))  # 移除第一个数字
        data_list[2] = 325  # 替换其中的元素
        return data_list

    # 字典
    def ds_dict(self):
        data_dict = {
            "name":"goblinM",
            "age":22,
            "gender":"female"
        }

        for k, v in data_dict.items():
            print("键是："+k+"值是："+str(v))
        print(list(data_dict.keys()))  # 获取所有的键
        print(list(data_dict.values()))  # 获取所有的值
        print(data_dict.pop('age'))  # 把键为age的东西都删除
        data_dict.setdefault("age",22)  # 设置键值对
        print(data_dict.get("name"))  # 获取键为name的值
        data_dict.update({"friend":"gg","favorite":"sleep"})  # 增加多个元素
        del data_dict["friend"]
        return data_dict

    # 元组
    def ds_tuple(self):
        data_tuple = ('a','b','c','d','e')
        return data_tuple[2]

    # 集合
    def ds_set(self):
        data_set = {1,2,3,4}
        two_set = {5,3,7,8}
        data_set.add(5)  # 添加元素
        data_set.update({6,7,8})  # 添加多个元素
        print(data_set)
        data_set.discard(5)  # 删除数字为5的元素
        data_set.remove(4)  # 移除数字为4的元素
        print(data_set)
        print(data_set.difference(two_set))  # 找出data_set不同于two_set的值
        print(data_set.intersection(two_set))  # 找出data_set和two_set的交集
        print(data_set.union(two_set))   # 联合data_set和two_set
        return data_set

    # 多重循环
    def ds_loop(self):
        num_list = [4,2,52,6,42,5]
        print(sorted(num_list,reverse=True))
        a = ['name',"age","favorite"]
        b = ["goblinM","22","sleep"]
        for i,j in zip(a,b):
            print(i+":"+j)

    # 推导式
    def ds_tuidao(self):
        a = [i for i in range(10)]
        print(a)
        b = {i:j for i in range(3) for j in ['a','b','c']}
        print(b)

    # 枚举获取索引
    def ds_enum(self):
        letters = ["a","b","c","d","e","f","g"]
        for index,letter in enumerate(letters):
            print("index:",index)
            print("letter:",letter)


if __name__ == "__main__":
    obj = DataStructureBase()
    print(obj.ds_list())
    print(obj.ds_dict())
    print(obj.ds_tuple())
    print(obj.ds_set())
    obj.ds_loop()
    obj.ds_tuidao()
    obj.ds_enum()