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
        file = r'D:\2022object\mall_api_test\testdata\1.jpeg'
        self.image = upload_image(file, self.token)

    @list_data(items)
    def test_admin_upload(self, items):
        """
        3.上传商品
        """
        # print("item", items)
        # projectInfo = """{
        #     "t": 1649503962366,
        #     "prodName": "好东西",
        #     "brief": "",
        #     "video": "",
        #     "prodNameEn": "好东西",
        #     "prodNameCn": "好东西",
        #     "contentEn": "",
        #     "contentCn": "",
        #     "briefEn": "",
        #     "briefCn": "",
        #     "pic": "2022/04/f414d8d9df274b909b959b579d67f88a.jpg",
        #     "imgs": "2022/04/f414d8d9df274b909b959b579d67f88a.jpg",
        #     "preSellStatus": 0,
        #     "preSellTime": null,
        #     "categoryId": 380,
        #     "skuList": [
        #         {
        #             "price": 0.01,
        #             "oriPrice": 0.01,
        #             "stocks": 0,
        #             "skuScore": 1,
        #             "properties": "",
        #             "skuName": "",
        #             "prodName": "",
        #             "weight": 0,
        #             "volume": 0,
        #             "status": 1,
        #             "prodNameCn": "好东西",
        #             "prodNameEn": "好东西"
        #         }
        #     ],
        #     "tagList": [
        #         2
        #     ],
        #     "content": "",
        #     "deliveryTemplateId": 1,
        #     "totalStocks": 0,
        #     "price": 0.01,
        #     "oriPrice": 0.01,
        #     "deliveryModeVo": {
        #         "hasShopDelivery": true,
        #         "hasUserPickUp": false,
        #         "hasCityDelivery": false
        #     }
        # }"""
        # 修改上传图片，添加token，发送接口
        url = 'http://mall.lemonban.com:8108/prod/prod'
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
