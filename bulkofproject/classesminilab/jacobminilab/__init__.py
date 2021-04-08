from flask import Blueprint, render_template, __name__, request

from bulkofproject.classesminilab.jacobminilab.jacoblab import Characters

jacobblueprint = Blueprint('jacob', __name__,
                           template_folder='templates')


@jacobblueprint.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST' :
        return render_template("jacob.html", Characters=Characters(int(request.form.get("series"))))
    return render_template("jacob.html", Characters=Characters(1))
