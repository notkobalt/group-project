#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
#import dylan lab
from bulkofproject.dylan.bubble import listgen, bubblesort
from bulkofproject.dylan.dylanlab import rsa

#create blueprint
dylandirectory = Blueprint('dylandirectory', __name__)

@dylandirectory.route('/bubble', methods = ['GET', 'POST'])
def bubble():
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

        return render_template('dylan/bubble.html', initial = initial, final = final)


    return render_template('bubblesortminilab/bubble.html')

@dylandirectory.route('/classes', methods = ['GET', 'POST'])
def classes():
    if request.method == 'POST':
        message = str(request.form.get('message'))
        key1 = int(request.form.get('key1'))
        key2 = int(request.form.get('key2'))

        encrypted = rsa(message, key1, key2)
        msg = encrypted.message
        k1 = encrypted.key1
        k2 = encrypted.key2
        final = encrypted.end
        clean = encrypted.endclean

        return render_template('dylan/classes.html', output = True, msg = msg, k1 = k1, k2 = k2, final = final, clean = clean)
    return render_template('dylan/classes.html')