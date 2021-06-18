#import flask and blueprints
from flask import Blueprint, render_template, __name__, request, session, redirect, url_for, flash
#import database
from bulkofproject.models import User
from bulkofproject import db

#create blueprint
account = Blueprint('account', __name__, template_folder = 'account')


@account.route('/profile')
def profile() :
    return render_template('account/profile.html')

@account.route('/login', methods = ['GET', 'POST'])
def login() :
    if request.method == 'POST':
        #set up future session data
        session.pop('user', None)
        session.permanent = True

        #get elements from front end
        username = request.form['username']
        password = request.form['password']

        #query database
        users = User.query.all()

        #check username/password match
        try:
            user = [user for user in users if user.username == username][0]
            #password match
            if user and user.password == password:
                #enter user into session
                session['user'] = user.username
                return redirect(url_for('home'))
            #no match
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for('account.login'))
        except:
            flash("Incorrect Username or Password")
            return redirect(url_for('account.login'))
    else:
        if 'user' in session:
            flash ("User Already Logged In")
            return redirect(url_for('home'))
        else:
            return render_template('account/login.html')


@account.route('/signup', methods = ['GET', 'POST'])
def signup() :
    if 'user' in session:
        flash ("User Already Logged In")
        return redirect(url_for('home'))
    elif request.method == 'POST':
        #get elements from front end
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmPassword']

        #check to see if passwords match
        if password == confirmpassword:
            commit = User(username = username, password = password)
            db.session.add(commit)
            db.session.commit()
            flash("User Successfully Created")
            return redirect(url_for('account.login'))
        else:
            flash("Passwords do not Match")
            return render_template('account/signup.html')
    else:
        return render_template('account/signup.html')

@account.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash("User Logged Out")
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))