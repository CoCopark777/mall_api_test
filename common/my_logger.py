# —— coding :utf-8 ——
# @time:    2020/9/23 21:13
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    my_logger.py
import logging


class MyLogger:
    def my_logger(self, msg, level):
        # 1.定义一个日志收集器
        logger = logging.getLogger()
        # 2. 设置级别
        logger.setLevel("DEBUG")
        # 3. 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 4. 创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh = logging.FileHandler('log.txt', encoding='UTF-8')
        fh.setLevel("WARNING")
        fh.setFormatter(formatter)
        # 5. 两者对接---指定输出渠道
        logger.addHandler(ch)
        logger.addHandler(fh)
        # 6. 收集日志
        if level == "DEBUG":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "WARNING":
            logger.warning(msg)
        elif level == "ERROR":
            logger.error(msg)
        elif level == "CRITICAL":
            logger.critical(msg)
        # 7. 关闭渠道
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.my_logger(msg, "DEBUG")

    def info(self, msg):
        self.my_logger(msg, "INFO")

    def warning(self, msg):
        self.my_logger(msg, "WARNING")

    def error(self, msg):
        self.my_logger(msg, "ERROR")

    def critical(self, msg):
        self.my_logger(msg, "CRITICAL")


if __name__ == '__main__':
    my_logger = MyLogger()
    my_logger.debug('debug级别信息！')
    my_logger.info('info级别信息！')
    my_logger.warning('warning级别信息！')
    my_logger.error('error级别信息！')
    my_logger.critical('critical级别信息！')
