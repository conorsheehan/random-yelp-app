"""
Request services for Yelp
"""

import json
import oauth2
import urllib
import urllib2
from yelp_api import yelp_settings

PATHS = {
    'search': '/v2/search'
}

SEARCH_PARAMS = (
    'term',
    'location',
    'bounds',
    'll',
    'offset',
    'limit',
    'cc',
    'lang',
    'cll',
    'radius_filter',
    'category_filter',
    'deals_filter',
    'sort',
)


class YelpRequest(object):

    """
    Yelp API request

    Client instructions:
    - Create new Request by providing a path_key (see PATHS) and url_params (see SEARCH_PARAMS)
    - Execute request with self.execute()
    """

    host = 'api.yelp.com'
    consumer_key = yelp_settings.API_V2_AUTH['consumer_key']
    consumer_secret = yelp_settings.API_V2_AUTH['consumer_secret']
    token = yelp_settings.API_V2_AUTH['token']
    token_secret = yelp_settings.API_V2_AUTH['token_secret']
    success = None

    def __init__(self, path_key, url_params=None):
        self.path = PATHS[path_key]
        self.encoded_params = self.encode_params(url_params)

    @property
    def url(self):
        return 'http://%s%s?%s' % (self.host, self.path, self.encoded_params)

    def encode_params(self, url_params):

        """
        Encode url parameters for queries.
        Limit the parameters to white-listed parameters
        """

        url_params = dict((param, val) for (param, val) in url_params.iteritems() if param in SEARCH_PARAMS)
        if url_params:
            return urllib.urlencode(url_params)
        else:
            return ''

    def execute(self):

        """
        Execute request
        """

        self.success = False
        signed_url = self.sign_url()

        # Connect
        try:
            conn = urllib2.urlopen(signed_url, None)
            try:
                response = json.loads(conn.read())
            finally:
                conn.close()
                self.success = True
        except urllib2.HTTPError, error:
            response = json.loads(error.read())

        return response

    def sign_url(self):

        """
        Returns signed url
        """

        consumer = oauth2.Consumer(self.consumer_key, self.consumer_secret)
        oauth_request = oauth2.Request('GET', self.url, {})
        oauth_request.update({
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': self.token,
            'oauth_consumer_key': self.consumer_key
        })

        token = oauth2.Token(self.token, self.token_secret)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        return oauth_request.to_url()
