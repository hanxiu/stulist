#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

import psycopg2
import psycopg2.pool

# 建立PostgreSQL数据库的连接池（全局）
dbconn_pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=2,
    maxconn=10,
    host='localhost', 
    database='stulist',
    user='dbo', 
    password='pass')


from contextlib import contextmanager
@contextmanager
def db_cursor():
    """ 创建数据库游标的上下文，方便执行SQL语句 """
    conn = dbconn_pool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        dbconn_pool.putconn(conn)



