#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        classroom    TEXT,     --班级
        sex     TEXT,        --性别
        birthday TEXT,        --出生日期
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name,classroom,sex,birthday)  VALUES 
        (101, '1310650313',  '叶航',  '信息1303',  '女','1995-01-15'), 
        (102, '1310650404',  '韩潇', '信息1304', '男','1996-06-22'),
        (103, '1310650316',  '黄晓旭', '信息1303', '女','1995-04-19'),
        (104, '1310650317',  '张著英', '信息1303', '女','1994-09-06'),
        (105, '1310650412',  '王学林', '信息1304', '男','1994-01-05');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')
