# -- encoding: utf-8 --
# @time:    	2022/4/8 21:15
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# test_case = [{"id": 1, "name": "a", "age": 18},
#              {"id": 2, "name": "b", "age": 19},
#              {"id": 3, "name": "c", "age": 20}]
import ddt
import unittest
from common.filehandle import test_data_path
from common.excelhandler import ExcelHandle
EH = ExcelHandle(file_name=test_data_path)
test_case = EH.read_all_data_lc('register')

def login(username=None, password=None):
    if username is None or password is None:
        return {"code": "500", "msg": "用户名或密码为空"}
    if username == 'zhangsan' and password == 123456:
        return {"code": "200", "msg": "登录成功"}
    return {"code": "500", "msg": "用户名或密码错误"}

# @ddt.ddt()
# class TestDtt(unittest.TestCase):
#     @ddt.data(*test_case)
#     def test_001(self, case_data):
#         # self.assert_(case_data["age"]>=19)
#         print(case_data)

@ddt.ddt()
class TestLogin(unittest.TestCase):

    @ddt.data(*test_case)
    def test_login_all(self, item):
        """测试函数当中不能随便加参数的。
        for item in items:
            创建一个函数test_login_all—_(item)
        """
        print("item",item)
        username = item["username"]
        password = item["password"]
        expected = item['expected']
        print(username,password,expected)
        actual = login(username, password)
        self.assertEqual(eval(expected), actual)

        # self.assertEqual(expected, str(actual))