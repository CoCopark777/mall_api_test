import time

import jsonpath
import requests
import uuid
import base64
import os
import sys
from testdata.back_conf import *
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
class Login:
    def __init__(self):
        self.t_id =int(time.time()*1000)
        self.uu_id =str(uuid.uuid4())
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}


    def get_image(self):
        url ="captcha.jpg"
        data ={"uuid":self.uu_id}
        res =requests.get(url,params=data)
        return res.content

    def get_image_number(self):
        image=self.get_image()
        base64_data=base64.b64encode(image)
        b64=base64_data.decode()
        # print("base64_data",base64_data)
        # print("b64", b64)

        url="http://api.ttshitu.com/predict"
        data={"username":"fishing",
              "password":"huqiang1992",
              "typeid":3,
              "image":b64}
        res =requests.post(url,json=data)
        number=res.json()["data"]["result"]
        return number

    def get_access_token(self):
        # number=self.get_image_number()
        # print(number)
        url= mall_back_url+ "adminLogin"
        data={
              "t": self.t_id,
              "principal": "student",
              "credentials": "123456a",
              "sessionUUID": self.uu_id,
              "imageCode": "lemon"
            }
        res =requests.post(url,json=data)
        print(res)
        token = jsonpath.jsonpath(res.json(), "$..access_token")[0]
        self.headers["Authorization"] = "bearer{}".format(token)
        return token

    def upload_image(self):
        file_name = os.path.join(path,'testdata','1.jpeg')
        url=mall_back_url + "admin/file/upload/img"
        files ={"file":("1.jpeg",open(file_name,"rb"),
                        'image/jpeg')}
        self.get_access_token()
        res =requests.post(url,files=files,headers=self.headers)
        return res.text

    def add_product(self):
        url=""
if __name__ == '__main__':
    # import uuid
    # print(uuid.uuid4())
    lg=Login()
    token = lg.get_access_token()
    print(token)
    res =lg.upload_image()
    print(res)


