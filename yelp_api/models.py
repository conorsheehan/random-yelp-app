"""
Yelp JSON models
"""


class YelpJSONDataObject(object):

    """
    Yelp object from a JSON request
    """

    DATA_ATTRIBUTES = ()

    def __init__(self, data):
        self.assign_data_attributes(data)

    def assign_data_attributes(self, data):

        """
        Assign attributes from data to class attributes
        """

        for attrib in self.DATA_ATTRIBUTES:
            if attrib.__class__ == tuple:
                val = globals()[attrib[1]](data[attrib[0]])
                attrib = attrib[0]
            elif attrib in data:
                val = data[attrib]
            else:
                val = None
            setattr(self, attrib, val)


class Business(YelpJSONDataObject):

    """
    Yelp Business (e.g. restaurant)
    """

    DATA_ATTRIBUTES = (
        'categories',  # List
        'display_phone',
        'id',
        'image_url',
        'is_claimed',
        'is_closed',
        ('location', 'Location'),  # Object
        'mobile_url',
        'name',
        'phone',
        'rating',
        'rating_img_url',
        'rating_img_url_large',
        'review_count',
        'snippet_image_url',
        'snippet_text',
        'url',
    )


class Location(YelpJSONDataObject):

    """
    Yelp business location
    """

    DATA_ATTRIBUTES = (
        'address',  # List
        'city',
        'country_code',
        'display_address',  # List
        'postal_code',
        'state_code',
    )


class SearchResults(YelpJSONDataObject):

    """
    Yelp search results object
    """

    DATA_ATTRIBUTES = (
        'region',  # List
        'total',
        'businesses',
    )

    def __init__(self, data):

        super(YelpJSONDataObject, self).__init__()
        #TODO: Allow data attributes to be looped over
        self.businesses = [Business(business_data) for business_data in data['businesses']]
