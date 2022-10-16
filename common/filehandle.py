# —— coding :utf-8 ——
# @time:    2020/9/23 22:04
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   492224300@qq.com
# @File:    file_dir.py
import os
# 基本路径
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 配置文件路径
case_config_path = os.path.join(base_path,'config','case.config')
# 测试数据路径
test_data_path = os.path.join(base_path,'testdata','test_cases.xlsx')
# 日志路径
log_path = os.path.join(base_path,'testresult','log')
# 测试报告路径
report_path = os.path.join(base_path,'testresult','html_report','api_test.html')
