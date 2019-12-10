# -*- encoding=utf-8 -*-
"""
这个是unittest对calculate的测试
"""

import unittest

from auto_test.unittest_calculate import Calculate


class ModuleTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        这个是初始化
        :return:
        """
        self.cal = Calculate(8, 4)

    def tearDown(self) -> None:
        """
        这个是结束测试用例后的动作
        :return:
        """
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
