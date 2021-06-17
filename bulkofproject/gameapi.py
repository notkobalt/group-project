from flask import Flask
from flask_restful import Api, Resource
import jsonify, json
import ssl

from bulkofproject.models import rating

app = Flask(__name__)
api = Api(app)

reviews = rating.query.all()
reviewjson = json.dumps(reviews)

class ratingData(Resource):
    def get(self, stars):
        return {"Info" : "hello"}
    def post(self):
        return {"Info": "Posted"}

print(reviewjson[2])
print(type(reviewjson))

api.add_resource(ratingData, "/ratingAPI/<int:stars>")

if __name__ == "__main__":
    app.run(debug = True)
