#import flask and blueprints
import requests
from flask import Blueprint, render_template, __name__, request
#import lab files
from bulkofproject.classesminilab.dylanlab import equations as equations
from bulkofproject.classesminilab.kiralab import Calc

lab = Blueprint('lab', __name__)

@lab.route('/dylan')
def dylan():
    x = 7

    #build class
    eqs = equations(x)

    return render_template('classesminilab/dylan.html', eqs = eqs.position)

@lab.route('/kira', methods = ["GET", "POST"])
def kira():
    if request.method =='POST':
        calculation = Calc(int(request.form.get("series")))
        return render_template(("classesminilab/kira.html"), calculation = calculation)
    return render_template('classesminilab/kira.html', calculation = Calc(5))


@lab.route('/jacob')
def jacob():
    return render_template('classesminilab/jacob.html')
