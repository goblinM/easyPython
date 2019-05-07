"""
created by goblinM 2019.5.7
字符串的基本用法
"""
#_*_

class StringBase:
    # 字符串的合并的+用法
    def str_join_add(self):
        one_add = "I"
        two_add = "Love"
        three_add = "coding"
        return one_add+two_add+three_add

    # 字符串的合并的join用法
    def str_join_join(self):
        str_list = ["I","Love","Coding"]
        return "".join(str_list)

    # 这个是join的一个比较有趣的点
    def str_join_join_special(self):
        one_list = "abc"
        two_list = ["laugh","may","ok"]
        return one_list.join(two_list)

    # 字符串的合并的替换用法(字符串的格式化)
    def str_join_replace(self):
        str_test = '%s%s%s' % ("I","Love","Coding")
        return str_test

    # 字符串的相乘
    def str_mul(self):
        word = "hello"
        return word*5

    #字符串的分片与索引
    def str_split_index(self):
        word = "I Love Coding!"
        print(word[0])  #第一个字符串
        print(word[2:5]) #取下标2开始，结束下标为4，左开右闭
        print(word[-1]) #最后一个字符串
        print(word[:4]) #取前四个字符串
        print(word[3:]) #取开始下标为3以后的所有的字符

    #字符串分片操作
    def str_find_evil(self):
        word = "superstar"
        str_evil = word[0]+word[2:-3]+word[-5:-3]
        return str_evil

    #字符串替换replace
    def str_replace(self):
        word = "I hate Coding!"
        return word.replace('hate','love '*5)

    #字符串的格式化
    def str_format(self):
        word1_format = "{} is cheap,show me the {}".format('talk','code')
        word2_format = "{w1} is cheap,show me the {w2}".format(w1='talk',w2='code')
        word3_format = "{0} is cheap,show me the {1}".format('talk','code')
        # format_map()这个是接受字典类型的
        mapping = {"w1":'talk',"w2":'code'}
        word4_format = "{w1} is cheap,show me the {w2}".format_map(mapping)
        print(word1_format)
        print(word2_format)
        print(word3_format)
        print(word4_format)


if __name__ == "__main__":
    obj = StringBase()
    print(obj.str_join_add())
    print(obj.str_join_join())
    print(obj.str_join_replace())
    print(obj.str_join_join_special())
    print(obj.str_mul())
    obj.str_split_index()
    print(obj.str_find_evil())
    print(obj.str_replace())
    obj.str_format()