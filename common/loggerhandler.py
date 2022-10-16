# -- encoding: utf-8 --
# @time:    	2022/4/10 20:10
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import logging
from logging import Logger
import os
import time

from common.filehandle import log_path
if not os.path.exists(log_path):
     os.mkdir(log_path)
# file_name = time.strftime('%Y%m%d%H%M%S',time.localtime())
file_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '.log'
logs_file = os.path.join(log_path, file_name)
class LoggerHandler(Logger):

    def __init__(self,
                 name='py_api_test',
                 level = 'DEBUG',
                 FileHandler_level = 'WARNING',
                 console_level = 'INFO',
                 format = '%(asctime)s-%(filename)s-%(lineno)d-%(name)s-%(levelname)s-日志信息:%(message)s',
                 file =logs_file):
        # 初始化收集器
        # logger = logging.getLogger(name)
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        formatter = logging.Formatter(format)
        # 初始化处理器
        if file:
            print(file)
            fh = logging.FileHandler(file,encoding='UTF-8')
            # 设置handler级别
            fh.setLevel(FileHandler_level)
            # 设置处理器输出格式 file_handler.setFormatter(fmt)
            fh.setFormatter(formatter)
            # 添加处理器 addHandler
            self.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch.setFormatter(formatter)
        self.addHandler(ch)

if __name__ == '__main__':
    # logger = LoggerHandler()
    # info_msg = 'info级别信息'
    # error_msg = 'error错误信息'
    # logger.error(error_msg)
    # logger.info(info_msg)
    pass