# 导包
import unittest

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./case")
# 获取文件流--> 指定报告写入的地点及文件名
with open("./report/text_report.txt", "w", encoding="utf-8") as f:
    unittest.TextTestRunner(stream=f).run(suite)
