import urllib.error
import urllib.parse
import urllib.request
import json

class Google_DistMatrix:

    def __init__(self, api_key):
        self.API_KEY = api_key
        self.BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

    # Given string formatted addresses, query Distance Matrix API for response
    def find_path(self, addresses):
        # join parts of the url into a single string
        params = urllib.parse.urlencode(
            {
                "origins" : addresses,
                "destinations" : addresses,
                "key" : self.API_KEY,
                "avoid" : "tolls"
            }
        )
        
        url = f"{self.BASE_URL}?{params}"
        
        print(url)
        
        try:
            response = urllib.request.urlopen(url)
        except urllib.error.URLError:
            print("urllib.error.URLError happend :)")
            print(urllib.error.URLError)
            exit(1)
        else:
            # if we didn't gte IOError, then parse the result
            result = json.load(response)
            # print(result)
            
        return result


    # DO NOT EDIT: Basic working version of Distance Matrix API
    def find_path_base(self):
        # join parts of the url into a single string
        params = urllib.parse.urlencode(
            {
                "origins" : "Sydney",
                "destinations" : "Mungo National Park",
                "key" : self.API_KEY
            }
        )
        
        url = f"{self.BASE_URL}?{params}"
        
        print(url)
        
        try:
            response = urllib.request.urlopen(url)
        except urllib.error.URLError:
            print("urllib.error.URLError happend :)")
            print(urllib.error.URLError)
        else:
            # if we didn't gte IOError, then parse the result
            result = json.load(response)
            print(result)
        