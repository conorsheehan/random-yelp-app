from yelp_api import search

# Test search
test_results = search(
    url_params={
        'location': "Boston",
        'term': "bars"
    }
)

# Print results
for business in test_results.businesses:
    print business.name
