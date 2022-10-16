# -- encoding: utf-8 --
# @time:    	2022/4/10 13:49
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import json
import sys
import time
import requests
from bs4 import BeautifulSoup
from testdata.back_conf import *
from common.loggerhandler import LoggerHandler
from common.filehandle import *
logger = LoggerHandler()


class ApiMethods(object):
    header = {'Accept': 'application/json, text/plain, */*',
              'Content-Type': 'application/json',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    def get_login_cookie(self, url, username):
        params = {"username": username}
        for i in range(5):
            except_values = []
            try:
                res = requests.get(url, headers=self.header, params=params, allow_redirects=False)
                cookie = res.cookies.get_dict()
                if cookie:
                    cookie_keys = list(cookie.keys())
                    if 'JARVIS_CURRENT_USER' in cookie_keys:
                        return cookie
                else:
                    time.sleep(10)
            except KeyError as e:
                except_values.append(eval(str(e)))
        else:
            sys.exit('login fail,please check test environment!')

    @staticmethod
    def read_json(json_data):
        path = os.path.join(base_path, 'resources', 'data', json_data)
        with open(path, 'r', encoding='utf-8') as f:
            body_json = json.loads(f.read())
            return body_json

    def http_request(self, method, url, kwargs):
        # 适用get、post、delete、put请求
        for i in range(3):
            try:
                res = requests.request(method, url, **kwargs)
                if res.status_code == 200:
                    try:
                        return res.status_code, res.json()
                    except:
                        return res.status_code, res.text
                else:
                    time.sleep(30)
            except requests.exceptions.RequestException as e:
                logger.warning(e)
        else:
            logger.error('调用接口三次均失败！')

    def http_post_request(self, cookie_url, url, username, payload, request_type='json', return_type='json',
                          cookie=None):
        """适用post的data、json请求格式"""
        i = 1
        while i < 4:
            try:
                if not cookie:
                    cookie = self.get_login_cookie(cookie_url, username)
                if request_type == 'json':
                    response = requests.post(url, headers=self.header, cookies=cookie, json=payload, timeout=60)
                else:
                    response = requests.post(url, headers=self.header, cookies=cookie, data=payload, timeout=60)
                status_code = response.status_code
                if status_code == 200:
                    body_text = response.text

                    if '<!DOCTYPE html>' in body_text:
                        soup = BeautifulSoup(body_text, 'lxml')
                        error = soup.find("div", class_='error-desc').text
                        if error:
                            logger.error('发送接口请求时出错，错误信息为-> %s' % error)
                            sys.exit("请人工检查一下错误提示信息！")

                    else:
                        if return_type == 'json':
                            try:
                                body_dict = response.json()
                                return body_dict
                            except ValueError as e:
                                logger.warning('%s' % e)
                                logger.warning('第%s次调用接口的响应体为->%s' % (i, body_text))
                        else:
                            return body_text
                else:
                    logger.warning('接口的响应状态码为{}-> 接口调用错误！'.format(status_code))
                    logger.warning('接口返回的消息体为-> %s' % response.text)
                i += 1
                time.sleep(5)

            except requests.exceptions.RequestException as e:
                logger.warning('%s' % e)
                i += 1
                time.sleep(5)
        else:
            logger.warning('重复调用接口3次，均为调用失败！')

    def http_get_request(self, url, cookie):
        for i in range(3):
            res = requests.get(url, cookies=cookie, headers=self.header, timeout=60)
            if res.status_code == 200:
                try:
                    body_json = res.json()
                    return body_json
                except ValueError as e:
                    logger.warning('%s' % e)
                    logger.warning(res.text)
            else:
                logger.warning('响应状态码为->%s，响应体为->%s' % (res.status_code, res.text))
                time.sleep(10)
        else:
            sys.exit('重复调用接口%s三次，均失败了！' % url)

    def prod_cetagory(self, payload):
        url = mall_back_url + 'prod/category'
        payload = {
            "t": 1650686838775,
            "categoryName": "冰墩墩2号",
            "categoryNameEn": "bingdundun",
            "status": 1,
            "seq": 1,
            "grade": 0,
            "parentId": 0,
            "pic": "2022/04/5443d863d3b044d9a1fbdfc33e29c25b.png",
            "icon": "2022/04/d56b7d9cf6544513bdf8a3882ca4ca06.jpg"
        }


if __name__ == '__main__':
    pass
