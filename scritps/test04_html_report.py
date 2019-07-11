# 导包
import unittest
from tool.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("../case")
# 获取文件流--> 指定报告写入的地点及文件名
with open("../report/html_report.html", "wb") as f:
    HTMLTestRunner(stream=f,
                   title="case项目自动化测试用例",
                   description="操作系统：win7").run(suite)
