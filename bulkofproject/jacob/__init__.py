from flask import request, Blueprint, render_template

from bulkofproject.jacob.sort import bubba

jacobdirectory = Blueprint('jacobdirectory', __name__)

@jacobdirectory.route('/bubble', methods=["GET", "POST"])
def sort():
    if request.form:
        all_list = []
        b = 1
        repeat = 5

        for i in range(repeat):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            all_list.append(int(user_input))
            b = b + 1
        bubble = bubba(all_list)

        return render_template('jacob/bubble.html', active_page='Jacob', testing=bubble)

    return render_template('jacob/bubble.html', active_page='Jacob')

@jacobdirectory.route('/classes')
def classes():
    return render_template('jacob/classes.html')

@jacobdirectory.route('/')
def Jacob() :
    return render_template('jacob/jacob.html')