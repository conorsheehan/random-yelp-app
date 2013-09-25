"""
Public methods for API use
"""

from yelp_api.services import YelpRequest
from yelp_api.models import SearchResults


def search(url_params):

    """
    Make a search request via Yelp API
    """

    search_request = YelpRequest('search', url_params=url_params)
    response = search_request.execute()

    return SearchResults(response)
