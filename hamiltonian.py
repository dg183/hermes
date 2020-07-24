import os
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import sys

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
        exit
    filename = sys.argv[1]
    
    
    # read file and get addresses
    addresses_str = read_addresses_str(filename)
        
    # find_path(addresses_str)
    find_path_return = {'destination_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'origin_addresses': ['9 Lorikeet St, Glenwood NSW 2768, Australia', '3 Gympie Pl, Wakeley NSW 2176, Australia', 'Shop+8/45-47 Smart St, Fairfield NSW 2165, Australia', '80 Melbourne Rd, St Johns Park NSW 2176, Australia'], 'rows': [{'elements': [{'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '28.9 km', 'value': 28879}, 'duration': {'text': '28 mins', 'value': 1706}, 'status': 'OK'}, {'distance': {'text': '20.7 km', 'value': 20675}, 'duration': {'text': '32 mins', 'value': 1914}, 'status': 'OK'}, {'distance': {'text': '31.1 km', 'value': 31065}, 'duration': {'text': '28 mins', 'value': 1668}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '28.4 km', 'value': 28427}, 'duration': {'text': '28 mins', 'value': 1700}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6083}, 'duration': {'text': '11 mins', 'value': 653}, 'status': 'OK'}, {'distance': {'text': '2.3 km', 'value': 2331}, 'duration': {'text': '5 mins', 'value': 285}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '19.9 km', 'value': 19869}, 'duration': {'text': '32 mins', 'value': 1891}, 'status': 'OK'}, {'distance': {'text': '6.1 km', 'value': 6081}, 'duration': {'text': '11 mins', 'value': 660}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6869}, 'duration': {'text': '13 mins', 'value': 759}, 'status': 'OK'}]}, {'elements': [{'distance': {'text': '31.3 km', 'value': 31346}, 'duration': {'text': '29 mins', 'value': 1723}, 'status': 'OK'}, {'distance': {'text': '2.5 km', 'value': 2516}, 'duration': {'text': '5 mins', 'value': 277}, 'status': 'OK'}, {'distance': {'text': '6.9 km', 'value': 6856}, 'duration': {'text': '12 mins', 'value': 737}, 'status': 'OK'}, {'distance': {'text': '1 m', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}]}], 'status': 'OK'}
    
    
    print(addresses_str)
    print("abc")
    print(API_KEY)
    
    print("Laters.")


# Given path to a csv file, this function will return an array with elements being each line in the file
def read_addresses_str(filename):
    addresses_list = []
    with open(filename) as file:
        for line in file:
            print(line)
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


def find_path(addresses):
    # join parts of the url into a single string
    params = urllib.parse.urlencode(
        {
            "origins" : addresses,
            "destinations" : addresses,
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
