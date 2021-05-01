#import flask and blueprints
import json
from flask import Blueprint, render_template, __name__, request
from bulkofproject.bubblesortminilab.kirabubble import Sort

#create blueprint
bubblesortminilab = Blueprint('bubble_sort', __name__)

@bubblesortminilab.route('/dylan', methods = ['GET', 'POST'])
def dylan():
    return render_template('bubblesortminilab/dylan.html')

@bubblesortminilab.route('/kira', methods = ['GET', 'POST'])
def kira():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("series") + "]")))
        return render_template(("bubblesortminilab/kira.html"), calculation = calculation, original = request.form.get("series"))
    return render_template(("bubblesortminilab/kira.html"), calculation = Sort([4, 27, 0, 9]), original = "")