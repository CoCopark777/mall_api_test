"""
登录接口
获取验证码接口
上传图片接口

"""
import uuid
import requests
import base64
import json


def get_img():
    """
    获取验证码二进制图片和uuid
    """
    # 验证码地址拼接
    url = 'http://mall.lemonban.com:8108' + '/captcha.jpg'
    uid = str(uuid.uuid4())
    res = requests.get(url)
    return res.content, uid


def base64_api(username, pwd, img, typeid):
    """
    获取验证码
    """
    url = 'http://api.ttshitu.com/predict'
    base64_data = base64.b64encode(img)
    b64 = base64_data.decode()
    data = {"username": username, "password": pwd, "typeid": typeid, "image": b64}
    res = requests.post(url, json=data)
    print(res.text)
    result = json.loads(res.text)
    return result['data']['result']

def admin_login(username, password, code='lemon'):
    """
    用户登录获取token
    """
    data = {"principal": username,
            "credentials": password,
            "imageCode": code}
    url = 'http://mall.lemonban.com:8108/adminLogin'
    response = requests.request("post", url, json=data)
    res = response.json()
    return res["access_token"]

def upload_image(file_path, token):
    """
    图片上传
    """
    url = 'http://mall.lemonban.com:8108/admin/file/upload/img'
    f = open(file_path, 'rb')
    headers = {"Authorization": f"Bearer{token}"}
    resp = requests.request('POST', url, files={'file': f}, headers=headers)
    f.close()
    # print(resp.text)
    return resp.text



# if __name__ == '__main__':
    # img1 = get_img()
    # print(img1[0])
    # res = base64_api(username="fishing", pwd="huqiang1992", typeid=3, img=img1[0])
    # print(res)
    # aa = admin_login(username="student", password="123456a")
    # bb = upload_image(r'D:\2022object\mall_api_test\testdata\1.jpeg', aa)




