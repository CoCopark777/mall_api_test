# -- encoding: utf-8 --
# @time:    	2022/4/10 18:22
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import unittest


class TestUnittestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    def setUp(self) -> None:
        print("setUp method")

    def tearDown(self) -> None:
        print("tearDown method")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_add(self):
        a = 1
        b = 2
        print("%s-> %s" % (self.__repr__, a + b))
        self.assert_(a>b)

    def test_subtraction(self):
        a = 1
        b = 2
        print("%s-> %s" % (self.__repr__, a - b))

    def test_sum(self):
        print("%s-> %s" % (self.__repr__, sum([i for i in range(100)])))

class TestUnittestDemo02(unittest.TestCase):
    def test_mul(self):
        print("%s-> %s" % (self.__repr__, 10*20))

if __name__ == '__main__':
    # import unittest
    import os
    import time
    from unittestreport import HTMLTestRunner

    # suite = unittest.defaultTestLoader.discover('./test_case', 'test*.py')

    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromName('test_add','test_unittest_demo')
    suite2 = loader.loadTestsFromModule("test_unittest_demo",pattern='test_subtraction')
    suite3 = loader.loadTestsFromTestCase(TestUnittestDemo02)
    suite = [suite1,suite2,suite3]
    local = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report_path = os.path.join(local, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    ts = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    file_name = 'api_test_{}.html'.format(ts)
    file_path = os.path.join(report_path, file_name)
    with open(file=file_path, mode='w', encoding='utf8') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='xxx项目接口测试报告', description='xxx接口用例', tester='jsonLiu')
        runner.run(suite)
