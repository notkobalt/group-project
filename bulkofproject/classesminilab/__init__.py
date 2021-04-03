#import flask and blueprints
from flask import Blueprint, render_template, __name__
#import lab files
from bulkofproject.classesminilab.dylanlab import equations as equations

lab = Blueprint('lab', __name__)

@lab.route('/dylan')
def dylan():
    x = 7

    #build class
    eqs = equations(x)

    return render_template('classesminilab/dylan.html', eqs = eqs.position)