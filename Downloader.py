import datetime
import json

from twarc import Twarc2, expansions
from Tokens import Topics

def download_tweets(start_date, end_date, lang_code, BEARER_TOKEN, topic, category):
    # Parse the start and end dates
    start_y, start_m, start_d = [int(x) for x in start_date.split("-")]
    end_y, end_m, end_d = [int(x) for x in end_date.split("-")]

    # Create start and end time periods in UTC
    start_time = datetime.datetime(
        start_y, start_m, start_d, 0, 0, 0, 0, datetime.timezone.utc
    )
    end_time = datetime.datetime(end_y, end_m, end_d, 0, 0, 0, 0, datetime.timezone.utc)

    t = Topics()
    query = t.make_query(lang_code, topic, category)
    
    # Instantiate the client
    client = Twarc2(bearer_token=BEARER_TOKEN)

    # Call the full-archive search endpoint to get tweets based on the input parameters
    search_results = client.search_all(
        query=query, start_time=start_time, end_time=end_time, max_results=100
    )

    # Return all tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the tweet information, the user, media etc. separately.
        # The method expansions.flatten allows us to get all the information in a single JSON
        result = expansions.flatten(page)

        # for tweet in result:
        #     # Print the full tweet object JSON to the console
        #     print(json.dumps(tweet))

        return result
