#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
#import dylan lab
from bulkofproject.bubblesortminilab.dylanlab import listgen, bubblesort

#create blueprint
bubblesortminilab = Blueprint('bubble_sort', __name__)

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