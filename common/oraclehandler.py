# -- encoding: utf-8 --
# @time:    	2022/4/6 22:22
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from time import sleep
import jaydebeapi
import os
import logging

logging.basicConfig(level=logging.INFO)


def jdbc_connect_oracle(user, psw, host, port, instance):
    db_url = "jdbc:oracle:thin:@%s:%s:%s" % (host, port, instance)
    driver = "oracle.jdbc.driver.OracleDriver"
    jar_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ojdbc7.jar")
    if os.path.exists(jar_file):
        conn = jaydebeapi.connect(driver, db_url, [user, psw], jar_file)
        cursor = conn.cursor()
        return conn, cursor
    else:
        logging.error('请确保jar包的路径正确且存在！')


def disconnect(conn, cursor):
    cursor.close()
    conn.close()


def query_all(sql, user, psw, host, port, instance):
    conn, cursor = jdbc_connect_oracle(user, psw, host, port, instance)
    i = 0
    while i < 30:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            disconnect(conn, cursor)
            return result
        i += 1
        sleep(30)
    else:
        logging.warning('在数据库循环查询15min均未查到数据')


def query_all_once(sql, user, psw, host, port, instance):
    conn, cursor = jdbc_connect_oracle(user, psw, host, port, instance)
    cursor.execute(sql)
    result = cursor.fetchall()
    disconnect(conn, cursor)
    return result


def query_one_once(sql, user, psw, host, port, instance):
    conn, cursor = jdbc_connect_oracle(user, psw, host, port, instance)
    cursor.execute(sql)
    result = cursor.fetchone()
    disconnect(conn, cursor)
    return result


def update_data(sql, user, psw, host, port, instance):
    conn, cursor = jdbc_connect_oracle(user, psw, host, port, instance)
    try:
        cursor.execute(sql)
        print("数据库中数据更新成功")
        sleep(5)
        disconnect(conn, cursor)
    except Exception as e:
        logging.error("SQL语句执行错误:%s" % e)


if __name__ == "__main__":
    pass
