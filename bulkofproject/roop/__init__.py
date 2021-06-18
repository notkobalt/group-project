#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
import json
#import dylan lab
from bulkofproject.dylan.dylanlab import listgen, bubblesort
from bulkofproject.kira.kirabubble import Sort

#create blueprint
roopdirectory = Blueprint('roopdirectory', __name__)

@roopdirectory.route('/bubble', methods = ['GET', 'POST'])
def roop():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("numbers") + "]")))
        return render_template(("bubblesortminilab/roop.html"), calculation = calculation, original = request.form.get("numbers"))
    return render_template(("bubblesortminilab/roop.html"), calculation = Sort([4, 27, 0, 9]), original = "")