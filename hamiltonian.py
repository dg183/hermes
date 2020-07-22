import os
import json
import time
import urllib.error
import urllib.parse
import urllib.request

def find_path():
    # join parts of the url into a single string
    params = urllib.parse.urlencode(
        {
            "origins" : "Sydney",
            "destinations" : "Mungo National Park",
            "key" : API_KEY
        }
    )
    
    url = f"{DIST_MATRIX_BASE_URL}?{params}"
    
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
    

# Get API key
API_KEY = os.environ.get("API_KEY_HERMES",'')
DIST_MATRIX_BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

# Required paramaters
    # origins
    # destinations
    # key

find_path()





print("abc")
print(API_KEY)

print("Laters.")