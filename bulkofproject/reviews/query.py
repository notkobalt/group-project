from bulkofproject.models import User, rating

def query():
    #empty list
    output = []

    #query database
    dbdict = rating.query.all()
    #create dictionary for every user
    for entry in dbdict:
        listentry = {'game':entry.game, 'stars':entry.stars, 'review':entry.review, 'user_review':entry.user, }
        #add dictionary to dict list
        output.append(listentry)
    return output