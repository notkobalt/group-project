#import flask and blueprints
from flask import Blueprint, render_template, __name__, request, session, redirect, url_for, flash
#other imports
import requests
from bulkofproject.models import db, rating
from bulkofproject.reviews.query import query
from bulkofproject.reviews.filter import filter

#create blueprint
reviews_bp = Blueprint('reviews', __name__, template_folder = '/reviews')

#display reviews
@reviews_bp.route('/', methods = ['GET', 'POST'])
def review():
    if 'user' in session:
        user = session['user']
    else:
        user = ""
    if request.method == 'POST':
        #query database
        origin = query()

        #pull from front end
        category = request.form['category']
        inputfilter = request.form['filter']

        #filter results
        display = filter(origin, category, inputfilter)
        return render_template('reviews/existing.html', user = user, display = display)
    else:
        display = query()
        print(display)
        return render_template('reviews/existing.html', user = user, display = display)

#search games
@reviews_bp.route('/search', methods = ['GET', 'POST'])
def search():
    if 'user' in session:
        user = session['user']
        if request.method == 'POST':
            #request
            titleslist = []
            titlesdictionary = {}
            displaylinks = ''
            searchurl = "https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&search="
            searchentry = request.form['search']
            searchlink = searchurl + searchentry

            searchresponse = requests.request("GET", searchlink)
            searchdump = searchresponse.json()
            searchresults = searchdump['results']

            #for display on front end
            for item in searchresults:
                titleslist.append(item['name'])

            for item in searchresults:
                titlesdictionary[item['name']] = item['background_image']

            #format for HTML
            displaylinks = ""
            for x, y in titlesdictionary.items():
                if y == None:
                    displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='bulkofproject/static/greysquare.jpg'><div class='title'>" + x + "</div></div></a>"
                else:
                    displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='" + y + "'><div class='title'>" + x + "</div></div></a>"

            #create session
            session.pop('results', None)
            session['results'] = titleslist

            return redirect(url_for('reviews.result'))
        else: return render_template(('reviews/search.html'), user = user)

    else:
        flash("please login before writing a review!")
        return redirect(url_for('reviews.result'))

#search output
@reviews_bp.route('/results', methods = ['GET', 'POST'])
def result():
    #user session
    if 'user' in session:
        user = session['user']
        #check for results
        if 'results' in session:
            if request.method == 'POST':
                gamepick = request.form['gamepick']
                session.pop('results', None)
                session.pop('reviewgame', None)
                session['reviewgame'] = gamepick

                return redirect(url_for('reviews.write'))
            else:
                #pull results from search page
                titleslist = session['results']

                return render_template('reviews/result.html', titleslist = titleslist, user = user)
        #if no results, redirect to search
        else:
            flash("redirecting to search...")
            return redirect(url_for('reviews.search'))
    else:
        return redirect(url_for('home'))


#post reviews
@reviews_bp.route('/write', methods = ['GET', 'POST'])
def write():
    if 'user' in session:
        user = session['user']
        if 'reviewgame' in session:
            game = session['reviewgame']
            if request.method == 'POST':
                stars = request.form['stars']
                writtenreview = request.form['review']

                reviewcommit = rating(game = str(game), stars = int(stars), review = str(writtenreview), user = str(user))
                db.session.add(reviewcommit)
                db.session.commit()
                flash("review posted successfully")
                return redirect(url_for('home'))
            else:
                return render_template('reviews/write.html', game = game, user = user)
        else:
            return redirect(url_for(review.search))
    else:
        flash("please sign in before accessing the rest of the website!")
        return redirect(url_for('home'))