from flask import request
from flask_login import UserMixin, current_user
from sqlalchemy import text

from __inputs__ import db, db_e



class User(db.Model, UserMixin): 
    '''
    Добавляет данные пользоватьеля в дб.
    '''
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(50), nullable = False)
    email =  db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(10000), nullable = False)

    def __init__(self, user_id, user_name, email, password):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = password

    def get_id(self):
        return self.user_id


def check_email_existion(email: str):
    '''
    Проверяет на наличие email в дб.
    '''
    ls = db_e.execute(text(f"""SELECT email FROM "users" where email = '{email}'""")).fetchone()

    if ls != None: ans = True
    else: ans = False

    return ans


def check_user_name_existion(user_name: str):
    '''
    Проверяет наличие user_name в дб.
    '''
    ls = db_e.execute(text(f"""SELECT email FROM "users" where user_name = '{user_name}'""")).fetchone()

    if ls != None: ans = True
    else: ans = False

    return ans


def add_new_User(user_name: str, email: str, password: hash):
    '''
    Добавляет нового пользователя.
    '''
    db_e.execute(text(f'''insert into users(
user_name, email, password)
values('{user_name}', '{email}', '{password}')'''))
    db_e.commit()


def for_add_rate():
    '''
    Получает инпуты со страницы рецензиии.
    '''
    meckanichs = int(request.form['mexaniki_input']);          plot = int(request.form['plot_input'])
    optimization = int(request.form['optimization_input']);      price = int(request.form['cost_input'])
    minuses = int(request.form['minus_input']);                vaib = int(request.form['vibe_input'])
    game_rate = rate_game(meckanichs, plot, optimization, price, minuses, vaib)

    titel = request.form['title_input']
    text = request.form['text_input']
    user_id = current_user.get_id()

    return meckanichs, plot, optimization, price, minuses, vaib, game_rate, titel, text, user_id


def rate_game(mechanics: int, plot: int, optimization: int, price: int, minuses: int, vibe: int):
    '''
    Высчитывание итоговой оценки для игры.
    '''
    rate = mechanics*1.8 + plot*1.9 + optimization*1.2 + price*1.1 + minuses*1.5 + vibe*2.5
    return int(rate)


def add_new_rate(table_name: str, data: for_add_rate):
    '''
    Добавляет новую рецензию.
    '''
    db_e.execute(text(f"""insert into "{table_name}"(
meckanichs, plot, optimization, price, minuses, vaib, game_rate, titel, text, user_id)
values({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, '{data[7]}', '{data[8]}', {data[-1]})"""))

    db_e.commit()


def check_existion_of_user_recession(name: str):
    '''
    Проверяет на наличие рецензии на игру у пользователя.
    '''
    usr_id = current_user.get_id()
    ls = db_e.execute(text(f"""SELECT user_id FROM "{name}" where user_id = '{usr_id}'""")).fetchone()

    if ls != None: ans = True
    else: ans = False

    return ans


def get_avg_game_rate(table_name: str):
    '''
    Получает среднюю оценку по 100 шкале.
    '''
    return db_e.execute(text(f"""select round(avg(game_rate)) from \"{table_name}\""""))


def get_rates_on_Game(name: str):
    '''
    Получает оценки со страницы.
    '''
    respose = db_e.execute(text(f"""select game_rate, titel, text, user_name from "{name}" as tab 
left join "users" as usr on tab.user_id = usr.user_id where text is not null and titel is not null limit 10"""))
    
    return respose

def get_quantity_of_rates(name: str):
    '''
    Получаем кол-во оценок на опр игру.
    '''
    resp = db_e.execute(text(f'select count(1) from "{name}"')).fetchall()

    if resp[0][0] == 0:
        st = 'рецензий'
    elif resp[0][0] == 1:
        st = 'рецензии'
    else:
        st = 'рецензиях'

    return [[resp, st]]
