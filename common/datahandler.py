# -- encoding: utf-8 --
# @time:    	2022/10/1 15:44
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from datetime import datetime


def handle_data(self, data):
    """
    :param data: 传入的数据信息
    :return: 递归过后的数据信息
    """
    # 1. 罗列各种情况 2. 针对不同的数据结构做不同的数据处理
    if isinstance(data, dict):
        #  如果是dict 就继续遍历 对应的value
        for key, value in data.items():
            data[key] = self.handle_data(value)

    elif isinstance(data, datetime):
        data = data
    elif isinstance(data, list):
        # 递归算法，如果是list 就继续遍历列表中的元素
        # data_new = []
        # for item in data:
        #     data_new.append(handle_data(item))
        # 把 原本的遍历操作使用列表推导式表达出来
        data = [self.handle_data(item) for item in data]
    elif isinstance(data, str):
        #    如果是str， 做+ "a"操作
        #
        # if "-" in data:
        #     pass
        data = data
    elif isinstance(data, bool):
        data = data
    elif isinstance(data, (int, float)):
        # 如果是整型或者float，做倍增
        data = data * 3
    else:
        # 如果是其他数据类型，保持原样
        data = data
    return data