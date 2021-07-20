import urllib.error
import urllib.parse
import urllib.request
import json

class Google_DistMatrix:

    def __init__(self, api_key):
        self.API_KEY = api_key
        self.BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

    # Given string formatted addresses, query Distance Matrix API for response
    def get_matrix(self, addresses):
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

        try:
            response = urllib.request.urlopen(url)
            result = json.load(response)
        except Exception as e:
            result = {
                'status': e
            }
            
        return result


    # DO NOT EDIT: Basic working version of Distance Matrix API
    def find_matrix_base(self):
        # join parts of the url into a single string
        params = urllib.parse.urlencode(
            {
                "origins" : "Sydney",
                "destinations" : "Mungo National Park",
                "key" : self.API_KEY
            }
        )
        
        url = f"{self.BASE_URL}?{params}"
                
        try:
            response = urllib.request.urlopen(url)
            result = json.load(response)
        except Exception as e:
            result = {
                'status': e
            }
            
        return result
        
    # Given a response from the Distance Matrix API
    # Output the matrix of paths between each node
    @staticmethod
    def print_matrix(api_response):
        # res = json.loads(api_response)
        nodes = api_response["destination_addresses"]
        rows = api_response["rows"]
        
        # print(nodes)
        # print(json.dumps(rows, indent=4))
        
        
        for row in rows:
            # print(row["elements"])
            for col in row["elements"]:
                # print(col)
                print(f'{col["distance"]["text"]},{col["duration"]["text"]}',end="")
                print(" | ",end="")
                
            print("<")

    # Given a response from Distance Matrix API
    # Return matrix of the travel times between nodes
    # Units = Seconds
    @staticmethod
    def matrix_by_time(api_response):
        rows = api_response["rows"]

        matrix = [[0 for x in range(len(rows))] for y in range(len(rows))]
        
        row_count = 0
        col_count = 0
        
        for row in rows:
            col_count = 0
            for col in row["elements"]:
                matrix[row_count][col_count] = col["duration"]["value"]
                col_count += 1
            row_count += 1
            
        return matrix

    # Given a response from Distance Matrix API
    # Return matrix of the distances between nodes
    # Units = Metres
    @staticmethod
    def matrix_by_distance(api_response):
        rows = api_response["rows"]

        matrix = [[0 for x in range(len(rows))] for y in range(len(rows))]
        
        row_count = 0
        col_count = 0
        
        for row in rows:
            col_count = 0
            for col in row["elements"]:
                matrix[row_count][col_count] = col["distance"]["value"]
                col_count += 1
            row_count += 1
            
        return matrix
