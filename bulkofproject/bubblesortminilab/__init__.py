#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
import json
#import dylan lab
from bulkofproject.bubblesortminilab.dylanlab import listgen, bubblesort
from bulkofproject.bubblesortminilab.kirabubble import Sort

#create blueprint
bubblesortminilab = Blueprint('bubble_sort', __name__)


@bubblesortminilab.route('/lucasbubble', methods = ['GET', 'POST'])
def lucasbubble():
    if request.method =='POST':
        calclist = Sort((json.loads("[" + request.form.get("numb") + "]")))
        return render_template(("bubblesortminilab/lucasbubble.html"), calclist = calclist)
        return render_template(("bubblesortminilab/lucasbubble.html"), calclist = Sort([]))

@bubblesortminilab.route('/dylan', methods = ['GET', 'POST'])
def dylan():
    if request.method == 'POST':
        initial = listgen(10)
        #sort type
        type = str(request.form['type'])

        #sort numbers
        if type == 'num':
            final = initial
            bubblesort(final)

        #sort alphabet
        if type == 'alph':
            initial1 = initial
            final1 = initial
            final1 = bubblesort(final1)
            initial = []
            final = []

            for integer in initial1:
                integer = chr(integer)
                initial.append(integer)

            for integer in final1:
                integer = chr(integer)
                final.append(integer)

        return render_template('bubblesortminilab/dylan.html', initial = initial, final = final)


    return render_template('bubblesortminilab/dylan.html')

@bubblesortminilab.route('/kira', methods = ['GET', 'POST'])
def kira():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("series") + "]")))
        return render_template(("bubblesortminilab/kira.html"), calculation = calculation, original = request.form.get("series"))
    return render_template(("bubblesortminilab/kira.html"), calculation = Sort([4, 27, 0, 9]), original = "")

@bubblesortminilab.route('/roop', methods = ['GET', 'POST'])
def roop():
    if request.method =='POST':
        calculation = Sort((json.loads("[" + request.form.get("numbers") + "]")))
        return render_template(("bubblesortminilab/roop.html"), calculation = calculation, original = request.form.get("numbers"))
    return render_template(("bubblesortminilab/roop.html"), calculation = Sort([4, 27, 0, 9]), original = "")
