from flask import Blueprint, render_template, __name__, request
import json
from bulkofproject.kira.kirabubble import Sort

lucasdirectory = Blueprint('lucasdirectory', __name__)

@lucasdirectory.route('/bubble', methods = ['GET', 'POST'])
def bubble():
    if request.method =='POST':
        calclist = Sort((json.loads("[" + request.form.get("numb") + "]")))
        return render_template(("lucas/bubble.html"), calclist = calclist)
    return render_template(("lucas/bubble.html"), calclist = Sort([]))

@lucasdirectory.route('/classes')
def classes():
    return render_template('lucas/classes.html')