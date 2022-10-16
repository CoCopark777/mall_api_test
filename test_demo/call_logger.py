# -- encoding: utf-8 --
# @time:    	2022/4/23 11:37
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from common.loggerhandler import LoggerHandler

logger = LoggerHandler()
if __name__ == '__main__':
    info_msg = 'info级别信息bbb'
    error_msg = 'error错误信息ccc'
    logger.error(error_msg)
    logger.info(info_msg)