import pymysql
from captcha.image import ImageCaptcha
from flask import g, current_app as app
import logging
import pandas as pd

def _connect_db():
    return pymysql.connect(
        host=app.config['MYSQL_DATABASE_HOST'],
        user=app.config['MYSQL_DATABASE_USER'],
        password=app.config['MYSQL_DATABASE_PASSWORD'],
        database=app.config['MYSQL_DATABASE_DB'],
        autocommit=True,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_db_rekonsiliasi():
    # tambahkan di __init__.py bagian function close_db
    if not hasattr(g, 'db_rekonsiliasi'):
        g.db_rekonsiliasi = _connect_db('db_rekonsiliasi')
    return g.db_rekonsiliasi


def get_db_admin():
    # tambahkan di __init__.py bagian function close_db
    if not hasattr(g, 'db_admin'):
        g.db_admin = _connect_db('db_admin')
    return g.db_admin


def get_db_ppob():
    # tambahkan di __init__.py bagian function close_db
    if not hasattr(g, 'db_ppob'):
        g.db_ppob = _connect_db('db_ppob')
    return g.db_ppob

def db_con():
    g.bagi_pulsa = _connect_db()
    return g.bagi_pulsa

def db_fetch(sql, param, rows=1):
    """
        rows = 1, return 1 row
        rows >1, return lebih dari 1 row
        return value berbentuk Pandas DataFrame
    """
    try:
        return pd.read_sql(sql, con=db_con(), params=param)
    except Exception as e:
        logging.error(e, exc_info=True)
        return None

def get_db_member_gdc():
    # tambahkan di __init__.py bagian function close_db
    if not hasattr(g, 'db_member_gdc'):
        g.db_member_gdc = _connect_db('db_member_gdc')
    return g.db_member_gdc

def db_exec(sql, param, insert_many=False):
    """ Untuk Insert, Update & Delete """
    try:
        with db_con() as con:
            with con.cursor() as cursor:
                if insert_many is True:
                    cursor.executemany(sql, param)
                else:
                    cursor.execute(sql, param)
                # lakukan commit bila tanpa row
                con.commit()
                return True
    except Exception as e:
        logging.error(e, exc_info=True)
        return False

def generate_captcha():
    pass
