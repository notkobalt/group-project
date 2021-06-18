#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
import json
#import dylan lab
from bulkofproject.dylan.bubble import listgen, bubblesort
from bulkofproject.kira.kirabubble import Sort

#create blueprint
roopdirectory = Blueprint('roopdirectory', __name__)

@roopdirectory.route('/bubble', methods = ['GET', 'POST'])
def bubble():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("numbers") + "]")))
        return render_template(("roop/bubble.html"), calculation = calculation, original = request.form.get("numbers"))
    return render_template(("roop/bubble.html"), calculation = Sort([4, 27, 0, 9]), original = "")

@roopdirectory.route('/classes')
def classes():
    return render_template('roop/classes.html')