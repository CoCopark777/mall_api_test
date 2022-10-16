# -- encoding: utf-8 --
# @time:    	2022/4/10 20:05
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import datetime
import threading
import logging
import requests
logging.basicConfig(level=logging.INFO)


class MyThring(threading.Thread):
    def __init__(self, func, args, name=''):
        super(MyThring, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):  # 重写run方法
        self.func(*self.args)


def task(ntask, nesc):
    # 任务
    start_time = datetime.datetime.now()
    logging.info("start task->(%s) time: %s" % (ntask, start_time))
    res = requests.get(url="http://www.baidu.com")
    print(res.text.encode('utf-8'))
    print(nesc)
    end_time = datetime.datetime.now()
    logging.info('end   task->(%s) time: %s' % (ntask, end_time))


def main(task_list):
    threads = []
    logging.info('start all time:  \t\t%s' % datetime.datetime.now())
    task_len = range(len(task_list))  # 任务列表长度
    for i in task_len:
        t = MyThring(task, (i, task_list[i]), task.__name__)
        threads.append(t)  # 把任务追加到线程列表
    for i in task_len:
        threads[i].start()  # 启动线程
    for i in task_len:
        threads[i].join()  # 等待子进程执行结束，阻塞
    logging.info('end   all time:  \t\t%s' % datetime.datetime.now())


if __name__ == '__main__':
    task_list = [10000, 1000000, 500, 100000000]
    main(task_list)