"""
上传商品用例

"""
import json
import unittest

from unittestreport import ddt, list_data
import requests
from config import Config

from common.apt_upload import admin_login, upload_image
from test_demo.call_excel import read_excel_dict

items = read_excel_dict(Config.CASE_FILE, 'addProduct')


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        1.登录获取token
        2.图片上传
        """
        # 登录
        self.token = admin_login(username="student", password="123456a")
        # 上传一张图片
        # file = r'D:\2022object\mall_api_test\testdata\1.jpeg'
        file = Config.CONFIG_DIR / 'testdata' / '1.jpeg'
        self.image = upload_image(file, self.token)

    @list_data(items)
    def test_admin_upload(self, items):
        """
        3.上传商品
        """
        url = items['url']
        projectInfo = items['json']
        # print(self.token)
        headers = {"Authorization": f"Bearer{self.token}"}
        data = json.loads(projectInfo)
        data['pic'] = self.image
        data['imgs'] = self.image

        response = requests.request("post", url, json=data, headers=headers)
        # print(response.text)

        # username = item["username"]
        # password = item["password"]
        # expected = item['expected']
        # print(username, password, expected)

        self.assertEqual(response.status_code == 200, True)

# if __name__ == '__main__':
