import os
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import sys
from graph import *

# ============== Helper func for displaying time
intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])
# ===========================================

# Get API key
API_KEY = os.environ.get("API_KEY_HERMES",'')
DIST_MATRIX_BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

# Required paramaters
    # origins
    # destinations
    # key

def main():
    # check for correct cmd line arguments ("python3 hamiltonian.py csv_file")
    if (len(sys.argv) != 2):
        print("Format: python3 hamiltonian.py <csv_file>")
        exit(1)
    filename = sys.argv[1]
    
    
    # read file and get addresses
    addresses_str = get_addresses_str(filename)
        
    find_path_return = find_path(addresses_str)

    if find_path_return['status'] != 'OK':
        print("Error: ", find_path_return['status'])
        exit(1)
    # find_path_return = {'destination_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'origin_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'rows': [{'elements': [{'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '28.9 km', 'value': 28879}, 'duration': {'text': '28 mins', 'value': 1706}, 'status': 'OK'}, {'distance': {'text': '20.7 km', 'value': 20675}, 'duration': {'text': '32 mins', 'value': 1914}, 'status': 'OK'}, {'distance': {'text': '31.1 km', 'value': 31065}, 'duration': {'text': '28 mins', 'value': 1668}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '28.4 km', 'value': 28427}, 'duration': {'text': '28 mins', 'value': 1700}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6083}, 'duration': {'text': '11 mins', 'value': 653}, 'status': 'OK'}, {'distance': {'text': '2.3 km', 'value': 2331}, 'duration': {'text': '5 mins', 'value': 285}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '19.9 km', 'value': 19869}, 'duration': {'text': '32 mins', 'value': 1891}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6081}, 'duration': {'text': '11 mins', 'value': 660}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6869}, 'duration': {'text': '13 mins', 'value': 759}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '31.3 km', 'value': 31346}, 'duration': {'text': '29 mins', 'value': 1723}, 'status': 'OK'}, {'distance': {'text': '2.5 km', 'value': 2516}, 'duration': {'text': '5 mins', 'value': 277}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6856}, 'duration': {'text': '12 mins', 'value': 737}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}]}], 'status': 'OK'}
    # find_path_return = {'destination_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'origin_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'rows': [{'elements': [{'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '19.0 km', 'value': 19007}, 'duration': {'text': '31 mins', 'value': 1886}, 'status': 'OK'}, {'distance': {'text': '20.7 km', 'value': 20675}, 'duration': {'text': '32 mins', 'value': 1914}, 'status': 'OK'}, {'distance': {'text': '20.5 km', 'value': 20531}, 'duration': {'text': '34 mins', 'value': 2035}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '19.0 km', 'value': 18985}, 'duration': {'text': '32 mins', 'value': 1931}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6083}, 'duration': {'text': '11 mins', 'value': 653}, 'status': 'OK'}, {'distance': {'text': '2.3 km', 'value': 2331}, 'duration': {'text': '5 mins', 'value': 285}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '19.9 km', 'value': 19869}, 'duration': {'text': '32 mins', 'value': 1891}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6081}, 'duration': {'text': '11 mins', 'value': 660}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6869}, 'duration': {'text': '13 mins', 'value': 759}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '20.8 km', 'value': 20834}, 'duration': {'text': '35 mins', 'value': 2077}, 'status': 'OK'}, {'distance': {'text': '2.5 km', 'value': 2516}, 'duration': {'text': '5 mins', 'value': 277}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6856}, 'duration': {'text': '12 mins', 'value': 737}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}]}], 'status': 'OK'}

    # print("==== addresses_str ====")
    # print(addresses_str)
    # print("==== find_path() return value ====")
    # print(json.dumps(find_path_return, indent=4))
    # print("==== matrix ====")
    # print_matrix(find_path_return)
    # print("==== matrix by time (seconds) ====")
    # print(matrix_by_time(find_path_return))
    # print("==== matrix by distance (metres) ====")
    # print(matrix_by_distance(find_path_return))
    # print("==== ==================== ====")
    
    G1 = Graph(find_path_return["destination_addresses"])
    # G1.graph = matrix_by_distance(find_path_return)
    G1.graph = matrix_by_time(find_path_return)
    # G1.hamCycle()

    path,trip_time = G1.solve()
    
    print_final_route(path,find_path_return["destination_addresses"],trip_time)


    
    print("Laters.")



def print_final_route(path, addr_list, trip_time):
    
    print("==================== FINAL ROUTE =================")
    
    print("ETA = ", display_time(trip_time))
    print("Number of stops = ", len(path))
    for v in path:
        print(addr_list[v])

    print("==================== END FINAL ROUTE =================")

    origin = addr_list[0].replace(' ','+')
    addr_list = addr_list[1:]

    print("==================== URL FOR ROUTE ===================")
    print("https://www.google.com/maps/dir/?api=1&origin=" + origin + "&waypoints=" + addresses_list_to_str(addr_list)[:-1])

    print("======================================================")




# Given path to a csv file, this function will return the parameter string for destination nodes
# for the Distance Matrix API
def get_addresses_str(filename):
    addresses_list = []
    with open(filename) as file:
        for line in file:
            # print(line)
            line = line.rstrip()
            addresses_list.append(line)
    
    addresses_str = addresses_list_to_str(addresses_list)
    
    return addresses_str
    
# Convert list of addresses to Distance Matrix API parameter string
def addresses_list_to_str(addr_list):
    addr_str = ""
    
    for addr_line in addr_list:
        words = addr_line.split(" ")
        for word in words:
            addr_str += word
            addr_str += "+"
        addr_str = addr_str[:-1]
        addr_str += "|"
        
    return addr_str

# Given a response from the Distance Matrix API
# Output the matrix of paths between each node
def print_matrix(api_response):
    # res = json.loads(api_response)
    nodes = api_response["destination_addresses"]
    rows = api_response["rows"]
    
    print(nodes)
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

# Given string formatted addresses, query Distance Matrix API for response
def find_path(addresses):
    # join parts of the url into a single string
    params = urllib.parse.urlencode(
        {
            "origins" : addresses,
            "destinations" : addresses,
            "key" : API_KEY,
            "avoid" : "tolls"
        }
    )
    
    url = f"{DIST_MATRIX_BASE_URL}?{params}"
    
    # print(url)
    
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print("urllib.error.URLError happend :)")
        print(urllib.error.URLError)
    else:
        # if we didn't gte IOError, then parse the result
        result = json.load(response)
        # print(result)
        
    return result


# DO NOT EDIT: Basic working version of Distance Matrix API
def find_path_base():
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
    
main()
