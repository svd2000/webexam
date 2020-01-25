from flask import Flask, request, render_template, session, redirect, url_for
from mysql_db import MySQL
import flask_login

app = Flask(__name__)
application = app

# app.config.from_pyfile('config.py')

# mysql = MySQL(app)

import MySQLdb
#import auth

# @app.route('/')
# def hello_world():
#     cursor = mysql.connection().cursor(named_tuple=True)
#     cursor.execute('select * from text;')
#     users = cursor.fetchall()
#     cursor.close()
#     return render_template('user_page.html', text=text)

# @app.route('/users/<int:id>')
# def show(id):
#     cursor = mysql.connection().cursor(named_tuple=True)
#     cursor.execute('select * from users where id=%s;', (id,))
#     user = cursor.fetchone()
#     cursor.close()
#     return render_template('show.html', user=user)
#ниже блок кода для работы с базой
#создаем подключение к БД
db = MySQLdb.connect(host="std-mysql.ist.mospolytech.ru", user="std_866", passwd="qwertyuio", db="py", charset='utf8')
#используя метод cursor() получаем объект для работы с базой
cursor = db.cursor()
#формируем sql запрос на запись
sql = """INSERT INTO test(test)
        VALUES ('%(zarplata)s')
        """%{"zarplata":test123}
# исполняем SQL-запрос
cursor.execute(sql)
# применяем изменения к базе данных
db.commit()