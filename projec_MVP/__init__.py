from flask import app, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from __inputs__ import app
from other import User, add_new_User, add_new_rate, for_add_rate, get_rates_on_Game, get_avg_game_rate
from other import check_existion_of_user_recession, check_email_existion, check_user_name_existion, get_quantity_of_rates
from email_validation import email_validaitor



login_manger = LoginManager(app)


@login_manger.user_loader
def load_user(user_id):
	return User.query.get(user_id)


@app.route("/")
def main_page():
    return render_template('MAIN.html')


@app.route("/catalog", methods = ['POST', 'GET'])
def catalog():
    spell_rate = get_avg_game_rate("The_Spell_Brigade_rates")
    MORDHAU_rate = get_avg_game_rate("MORDHAU_rates")

    will_rate = get_avg_game_rate("Will_To_Live_Online_rates")
    eft_rate = get_avg_game_rate("Escape_From_Tarkov_rates")

    starv_rate = get_avg_game_rate("Dont_Starve_Together_rates")
    verdun_rate = get_avg_game_rate("Verdun_rates")

    eden_rate = get_avg_game_rate("Eden_Crafters_rates")
    SOMA_rate = get_avg_game_rate("SOMA_rates")

    return render_template("CATALOG.html", spell_rate=spell_rate, MORDHAU_rate=MORDHAU_rate, will_rate=will_rate,
                           eft_rate=eft_rate, starv_rate=starv_rate, verdun_rate=verdun_rate,
                           eden_rate=eden_rate, SOMA_rate=SOMA_rate)


@app.route("/registration", methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash('Пароли не совпадают')
            return redirect(url_for('registration'))

        elif check_email_existion(email) == True:
            flash('Такой адрес электронной почты уже зарегестрирован.')
            return redirect(url_for('registration'))

        elif check_user_name_existion(user_name) == True:
            flash('Такой никнейм уже зарегестрирован.')
            return redirect(url_for('registration'))

        elif not email_validaitor(email):
            flash('Email не действителен.')
            return redirect(url_for('registration'))

        else:
            password = generate_password_hash(password)
            add_new_User(user_name, email, password)

            return redirect(url_for('login_page'))
    else: 
        return render_template('REGISTER.html')


@app.route('/login', methods = ['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
										
        temp_user = User.query.filter_by(email=email).first()
											
        if not temp_user:
            flash('Email недействителен.')
            return redirect(url_for('login_page'))
        elif  not check_password_hash(temp_user.password, password):
            flash('Неправильный пароль.')
            return redirect(url_for('login_page'))
        else:								
            login_user(temp_user)                                                  
            return redirect(url_for('main_page')) 									
    else:
        return render_template('LOGIN.html')



@app.route('/rates_of_The_Spell_Brigade')
def rates_of_The_Spell_Brigade():
    name = 'The_Spell_Brigade_rates'
    data =  get_rates_on_Game(name)
    spell_rate = get_avg_game_rate("The_Spell_Brigade_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/The_Spell_Brigade_rates.html", data=data, rate=spell_rate, recs=recs, st=st)

@app.route('/rate_The_Spell_Brigade', methods = ['POST', "GET"])
@login_required
def rate_The_Spell_Brigade():
    name = 'The_Spell_Brigade_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_The_Spell_Brigade'))
    else:
        spell_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_The_Spell_Brigade'))
        else:
            return render_template("games/The_Spell_Brigade_recension.html", rate = spell_rate)
    


@app.route('/rates_of_MORDHAU')
def rates_of_MORDHAU():
    name = 'MORDHAU_rates'
    data =  get_rates_on_Game(name)
    MORDHAU_rate = get_avg_game_rate("MORDHAU_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/MORDHAU_rates.html", data=data, rate=MORDHAU_rate, recs=recs, st=st)

@app.route('/rate_MORDHAU', methods = ['POST', "GET"])
@login_required
def rate_MORDHAU():
    name = 'MORDHAU_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_MORDHAU'))
    else:
        MORDHAU_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_MORDHAU'))
        else:
            return render_template("games/MORDHAU_recension.html", rate = MORDHAU_rate)



@app.route('/rates_of_Will_To_Live_Online')
def rates_of_Will_To_Live_Online():
    name = 'Will_To_Live_Online_rates'
    data =  get_rates_on_Game(name)
    will_rate = get_avg_game_rate("Will_To_Live_Online_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/Will_To_Live_Online_rates.html", data=data, rate=will_rate, recs=recs, st=st)

@app.route('/rate_Will_To_Live_Online', methods = ['POST', "GET"])
@login_required
def rate_Will_To_Live_Online():
    name = 'Will_To_Live_Online_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_Will_To_Live_Online'))
    else:
        will_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_Will_To_Live_Online'))
        else:
            return render_template("games/Will_To_Live_Online_recension.html", rate = will_rate)



@app.route('/rates_of_Escape_From_Tarkov')
def rates_of_Escape_From_Tarkov():
    name = 'Escape_From_Tarkov_rates'
    data =  get_rates_on_Game(name)
    eft_rate = get_avg_game_rate("Escape_From_Tarkov_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/Escape_From_Tarkov_rates.html", data=data, rate=eft_rate, recs=recs, st=st)

@app.route('/rate_Escape_From_Tarkov', methods = ['POST', "GET"])
@login_required
def rate_Escape_From_Tarkov():
    name = 'Escape_From_Tarkov_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_Escape_From_Tarkov'))
    else:
        eft_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_Escape_From_Tarkov'))  
        else:
            return render_template("games/Escape_From_Tarkov_recension.html", rate = eft_rate)



@app.route("/rates_of_Dont_Starve_Together")
def rates_of_Dont_Starve_Together():
    name = "Dont_Starve_Together_rates"
    data =  get_rates_on_Game(name)
    starv_rate = get_avg_game_rate("Dont_Starve_Together_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/Dont_Starve_Together_rates.html", data=data, rate=starv_rate, recs=recs, st=st)

@app.route("/rate_Don't_Starve_Together", methods = ['POST', "GET"])
@login_required
def rate_Dont_Starve_Together():
    name = 'Dont_Starve_Together_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_Dont_Starve_Together'))
    else:
        starv_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_Dont_Starve_Together'))     
        else:
            return render_template("games/Dont_Starve_Together_recension.html", rate = starv_rate)
    


@app.route("/rates_of_Verdun")
def rates_of_Verdun():
    name = 'Verdun_rates'
    data =  get_rates_on_Game(name)
    verdun_rate = get_avg_game_rate("Verdun_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/Verdun_rates.html", data=data, rate=verdun_rate, recs=recs, st=st)

@app.route('/rate_Verdun', methods = ['POST', "GET"])
@login_required
def rate_Verdun():
    name = 'Verdun_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_Verdun'))
    else:
        verdun_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_Verdun'))
        else:
            return render_template("games/Verdun_recension.html", rate = verdun_rate)
    


@app.route('/rates_of_Eden_Crafters')
def rates_of_Eden_Crafters():
    name = 'Eden_Crafters_rates'
    data =  get_rates_on_Game(name)
    eden_rate = get_avg_game_rate("Eden_Crafters_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/Eden_Crafters_rates.html", data=data, rate=eden_rate, recs=recs, st=st)

@app.route('/rate_Eden_Crafters', methods = ['POST', "GET"])
@login_required
def rate_Eden_Crafters():
    name = 'Eden_Crafters_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_Eden_Crafters'))
    else:
        eden_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_Eden_Crafters'))
        else:
            return render_template("games/Eden_Crafters_recension.html", rate = eden_rate)



@app.route('/rates_of_SOMA')
def rates_of_SOMA():
    name = 'SOMA_rates'
    data =  get_rates_on_Game(name)
    SOMA_rate = get_avg_game_rate("SOMA_rates")
    recs = get_rates_on_Game(name)
    st = get_quantity_of_rates(name)
    return render_template("games/SOMA_rates.html", data=data, rate=SOMA_rate, recs=recs, st=st)

@app.route('/rate_SOMA', methods = ['POST', "GET"])
@login_required
def rate_SOMA():
    name = 'SOMA_rates'
    if check_existion_of_user_recession(name) == True:
        flash('Вы уже оставиль рецензию на эту игру.')
        return redirect(url_for('rates_of_SOMA'))
    else:
        SOMA_rate = get_avg_game_rate(name)

        if request.method == 'POST':
            fer = for_add_rate()
            add_new_rate(name, fer)

            return redirect(url_for('rates_of_SOMA'))
        else:
            return render_template("games/SOMA_recension.html", rate = SOMA_rate)




@app.after_request
def redirect_to_login_page(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)