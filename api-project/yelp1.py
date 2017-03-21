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

params = {
    'term': 'Asia food',
    'lang': 'fr'
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





