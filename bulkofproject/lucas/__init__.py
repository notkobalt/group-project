from flask import Blueprint, render_template, __name__, request
import json
from bulkofproject.lucas.lucasbubble import bubble

lucasdirectory = Blueprint('lucasdirectory', __name__)

@lucasdirectory.route('/bubble', methods = ['GET', 'POST'])
def bubble():
    if request.method =='POST':
        calclist = bubble((json.loads("[" + request.form.get("numb") + "]")))
        return render_template(("lucas/bubble.html"), calclist = calclist)
    return render_template(("lucas/bubble.html"), calclist = bubble([]))

@lucasdirectory.route('/classes')
def classes():
    return render_template('lucas/classes.html')