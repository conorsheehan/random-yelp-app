import json
from settings_secret import API_V2_AUTH
from yelp_api.services import request

test_1 = request(
    host='api.yelp.com',
    path='/v2/search',
    url_params={
        'location': "Boston",
        'location': "bars",
    },
    consumer_key=API_V2_AUTH['consumer_key'],
    consumer_secret=API_V2_AUTH['consumer_secret'],
    token=API_V2_AUTH['token'],
    token_secret=API_V2_AUTH['token_secret']
)
print json.dumps(test_1, sort_keys=True, indent=2)
