from flask import Blueprint, render_template, __name__

lab = Blueprint('lab', __name__)

@lab.route('/dylan')
def dylan():
    return render_template('classesminilab/dylan.html')