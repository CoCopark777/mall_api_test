# -- encoding: utf-8 --
# @time:    	2022/4/6 22:24
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# 安装：pip install unittestreport

"""
用例收集

1、加载器defaultTestLoader()
testloader =unittest.defaultTestLoader()

2、查找测试用例，加载用例，得到的就是测试套件
suite =testloader.discover(start_dir, pattern='test*.py')
参数说明：
start_dir：测试用例文件目录
pattern='test*.py'：测试用例文件名称，默认以test开头的py文件

3、运行器
runner = unittest.TextTestRunner()
runner.run(suite)
"""
import unittest
import os
from unittestreport import TestRunner
import time

file_name=os.path.dirname(__file__)
case_path =os.path.join(file_name,'testcase')
report_path =os.path.join(file_name,'testresult','report')


#1、加载器，加载测试用例
testloader =unittest.TestLoader()  #创建收集器
#2、收集器，收集测试用例
print(case_path)
suite=testloader.discover(case_path, pattern='test*.py')
#3、运行器,运行收集到的测试用例
# runner =unittest.TextTestRunner()
# runner.run(suite)
st =str(int(time.time()))

runner = TestRunner(
                 suite=suite,
                 filename="my_report{}.html".format(st),
                 report_dir=report_path,
                 title='接口测试报告',
                 tester='testuser',
                 desc="接口自动化测试",
                 templates=2
)
runner.run()



# runner.send_email(
#                   host="smtp.qq.com",
#                   port=465,
#                   user="xxxx@qq.com",
#                   password="123456",
#                   to_addrs=["xxxxx@163.com"]
# )

# from BeautifulReport import BeautifulReport
# runner = BeautifulReport(suite)
# runner.report(description='接口单元测试',report_dir=report_path,filename='beaufiful_report_{}.html'.format(st))