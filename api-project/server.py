
from flask import Flask,render_template,request

import yelp1
import os
import yelp


from secret import CONSUMER_KEY,CONSUMER_SECRET,TOKEN,TOKEN_SECRET
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    token=TOKEN,
    token_secret=TOKEN_SECRET
)

client = Client(auth)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("yelp-web.html")

@app.route('/input')
def input():
    keyword = request.args.get("keyword")
    
    params = {
        'term': 'Asia food',
        'lang': 'en'
    }

    client.search('San Francisco', **params)

    client.search_by_bounding_box(
        37.900000,
        -122.500000,
        37.788022,
        -122.399797,
        **params
    )

    response = client.search_by_coordinates(37.788022, -122.399797, **params)

    name = (response.businesses[0].name)
    url = (response.businesses[0].url)
    rating = (response.businesses[0].rating)
    address = (response.businesses[0].location.address)


    print (name)
    print (type(name))
    print (url)
    print (type(url))

    return render_template("yelp-result.html",
                            name=name,
                            link=url)





    


if __name__ == "__main__":
    app.run(debug=True)
