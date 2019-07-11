"""
    目标：跳过用例
    方法：
    1.@unittest.skip(原因) # 直接跳过 不关注条件是否满足
    2.@unittest.skipif(条件,原因) # 条件满足，跳过用例
"""

# 导包
import unittest
reason = 4


# 新建测试类 并继承
class Test01(unittest.TestCase):
    
    def test001(self):
        print("Test01-->test001被执行")

    @unittest.skipIf(reason > 3, "未完成，用例不执行")
    def test002(self):
        print("Test01-->test002被执行")

    def test003(self):
        print("Test01-->test003被执行")