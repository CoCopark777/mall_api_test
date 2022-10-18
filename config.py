"""
读取路径

"""


import pathlib


class Config:
    HOST = 'http://mall.lemonban.com:8108'
    # CONFIG_DIR = pathlib.Path('.').absolute()

    CONFIG_FILE = pathlib.Path(__file__).absolute()
    CONFIG_DIR = CONFIG_FILE.parent

    # 项目的根目录
    ROOT = CONFIG_DIR
    # 测试用例的路径
    CASE_FILE = ROOT / 'testdata' / 'cases.xlsx'
    # 日志存储的路径
    LOG_FILE = ROOT / 'testresult' / 'log'