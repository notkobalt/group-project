#imports
##import config from __init__
from flask import render_template
from bulkofproject import app

#run project
if __name__ == '__main__':
    app.run(debug = True)