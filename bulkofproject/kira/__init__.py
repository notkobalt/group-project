from flask import Blueprint, render_template, __name__, request
import json
from bulkofproject.kira.kirabubble import Sort
from bulkofproject.kira.kiralab import Calc

kiradirectory = Blueprint('kiradirectory', __name__)

@kiradirectory.route('/bubble', methods = ['GET', 'POST'])
def bubble():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("series") + "]")))
        return render_template(("kira/kirabubble.html"), calculation = calculation, original = request.form.get("series"))
    return render_template(("kira/kirabubble.html"), calculation = Sort([4, 27, 0, 9]), original = "")

@kiradirectory.route('/classes', methods = ["GET", "POST"])
def classes():
    if request.method =='POST':
        calculation = Calc(int(request.form.get("series")))
        return render_template(("classesminilab/kirabubble.html"), calculation = calculation)
    return render_template('classesminilab/kirabubble.html', calculation = Calc(5))

@kiradirectory.route('/')
def Kira() :
    return render_template('kira/kira.html')