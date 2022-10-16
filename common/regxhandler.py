# -- encoding: utf-8 --
# @time:    2020/12/13 0:21
# @Author: jsonLiu
# @Email: 492224300@qq.com
# @file: regxhandler.py
import re


class RegxHandler(object):
    @staticmethod
    def universal_regx_handler(custom_pattern, str):
        data = re.search(custom_pattern, str)
        return data

    @staticmethod
    def str_substitute(custom_pattern, new, str, count=1):
        new_str = re.sub(custom_pattern, new, str, count=count)
        return new_str

    @staticmethod
    def match_qq(str):
        # re.compile()将正则表达式编译成Pattern对象
        pattern = re.compile(r'[1-9][0-9]{4,9}')
        return re.search(pattern, str)

    @staticmethod
    def match_mobile_phone(str):
        pattern = re.compile(r'1[35789]\d{9}')
        return re.search(pattern, str)

    @staticmethod
    def match_email(str):
        pattern = re.compile(r'\w{5,20}@(163|126|qq|139)\.(com|cn)')
        return re.search(pattern, str)

    @staticmethod
    def match_username(str):
        pattern = re.compile(r'[a-zA-Z_0-9]{5,20}')
        # pattern = re.compile(r'\w{5,20}')
        return re.search(pattern, str)

    @staticmethod
    def match_domain_name(str):
        # 匹配域名
        pattern = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')
        return re.search(pattern, str)


if __name__ == '__main__':
    regx = RegxHandler()
    # str = 'abJsonabcAbc'
    # custom_pattern = 'abc'
    # data = regx.universal_regx_handler(custom_pattern,str)
    # print(data)
    qq = 'aafqq:aa4922243001111ssssaaabbn'
    data = regx.match_qq(qq)
    print(data)

    str = "[jfjaognag.jpg] http://map.baidu.cn http:www.runoob.com"
    res = regx.match_domain_name(str=str)
    print(res)
