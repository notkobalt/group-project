#import flask and blueprints
import requests
from flask import Blueprint, render_template, __name__, request
#import lab files
from bulkofproject.classesminilab.dylanlab import rsa as rsa

from bulkofproject.classesminilab.kiralab import Calc

lab = Blueprint('lab', __name__)

@lab.route('/dylan', methods = ['GET', 'POST'])
def dylan():
    if request.method == 'POST':
        message = str(request.form.get('message'))
        key1 = int(request.form.get('key1'))
        key2 = int(request.form.get('key2'))

        encrypted = rsa(message, key1, key2)
        msg = encrypted.message
        k1 = encrypted.key1
        k2 = encrypted.key2
        final = encrypted.end

        return render_template('classesminilab/dylan.html', output = True, msg = msg, k1 = k1, k2 = k2, final = final)
    return render_template('classesminilab/dylan.html')

@lab.route('/kira', methods = ["GET", "POST"])
def kira():
    if request.method =='POST':
        calculation = Calc(int(request.form.get("series")))
        return render_template(("classesminilab/kira.html"), calculation = calculation)
    return render_template('classesminilab/kira.html', calculation = Calc(5))


@lab.route('/jacob')
def jacob():
    return render_template('classesminilab/jacob.html')
