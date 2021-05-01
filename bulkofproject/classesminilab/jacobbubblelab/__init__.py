from flask import request, Blueprint, render_template

from bulkofproject.classesminilab.jacobbubblelab.sort import bubba

jacobbubblesort = Blueprint('jacobbubble', __name__,
                            template_folder='/bubblesortminilab')


@jacobbubblesort.route('/', methods=["GET", "POST"])
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

        return render_template('bubblesortminilab/jacobbubble.html', active_page='Jacob', testing=bubble)

    return render_template('bubblesortminilab/jacobbubble.html', active_page='Jacob')
