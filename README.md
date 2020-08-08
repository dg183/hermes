# hermes

Optimal route finder for multiple stops using the Google Maps API

To run:
`python3 hamiltonian.py <suburb>.csv [optional database, default=addresses/db.csv]`

## Have a go
`python3 hamiltonian.py addresses/prospect.csv addresses/example_db.csv`


## Required files
`addresses/db.csv` - Database of all orders and addresses
* example [here](addresses/example_db.csv)
* **TAB** separated values (TSV) file
* Columns: Name, zID, Email, Phone, Beige size, Rose size, Shirt size, Champion hoodie size, Address, Suburb

`addresses/<suburb>.csv` - List of addresses in route
* example [here](addresses/prospect.csv)
* **Limit of 10 addresses per CSV (limited by Distance Matrix API)**
* Note: `suburb` in `<suburb>.csv` should match `suburb` field in `db.csv`


# Notes
## Project requirements
Drivers will depart from home and travel to each address within their surrounding suburb.

Optimal path will be the path with shortest travel time. This path must create a circuit with the driver's home as the start and end location, passing through every delivery address at least once.


## API time complexity
Given a list of `origins` and `destinations`, the API will return an array of distances between from each origin to each destination.

    * array of size `origins` x `destinations` 
    * O(sizeof(`origins`) * sizeof(`destinations`)) 
    
For our application, we have a list of locations, and want to find the optimal route between them all. Therefore, origins = destinations

    * Suppose we have `n` addresses
    * Return array is size `n^2`
    * Time complexity = `O(n^2)`


## Address input format
Input from CSV files.

We can either have one large CSV with all addresses, or manually separate by suburb.

Time complexity
* assuming 5 suburbs with equal destinations
* Total number of addresses = `n`

Single CSV | Separated by suburb
--- | ---
`O(n^2)` | `O(5*(n/5)^2) = O(n^2/5)`

For 100 addresses,

Single CSV | Separated by suburb
--- | ---
`O(100^2) = O(10,000)` | `O(100^2/5) = O(2,000)`

**Much more worth to separate by suburb with multiple smaller CSV's.**

## Pricing of Distance Matrix API
developers.google.com/maps/documentation/distance-matrix/usage-and-billing

Each query sent to the Distance Matrix API generates elements, where the number of `origins` times the number of `destinations` equals the number of elements.

### SKU: Distance Matrix (Price per ELEMENT - Monthly)
0 - 100,000 | 100,001 - 500,000 | 500,000+
--- | --- | ---
0.005 USD per ELEMENT (5.00 USD per 1000) | 0.004 USD per ELEMENT (4.00 USD per 1000) | Contact Sales for volume pricing

### SKU: Distance Matrix Advanced (Price per ELEMENT - Monthly)
0 - 100,000 | 100,001 - 500,000 | 500,000+
--- | --- | ---
0.01 USD per ELEMENT (10.00 USD per 1000) | 0.008 USD per ELEMENT (8.00 USD per 1000) | Contact Sales for volume pricing

## Usage limits
* There is no limit on the maximum number of elements per day (EPD)
* Maximum of 25 origins or 25 destinations per request
* Maximum of 100 elements per server-side request
* Maximum of 100 elements per client-side request
* 1000 elements per second (EPS), calculated as the sum of client-side and server-side queries


# Functions

## print_final_route(path, addr_list, trip_time)
Input: List of optimal path from start to end, List of addresses, Total trip time

Output: ETA, Number of stops, (Address,Name,Order contents,Mobile) for each destination, and URL with route inputted into Google Maps

## get_addresses_str(filename)
Input: Path to file (e.g. `addresses/blacktown.csv`)

Output: String formatted for `destinations` parameter of Distance Matrix API (e.g. `123+Cherry+St.+Chazza+NSW+1234|456+Parrot+Land,+Wakeley+8421|54+Monkey+Road,+Wahoo,+NSW,+124|`)

## addresses_list_to_str(addr_list)
**Called by get_addresses_str()**

Input: List of addresses

Output: String formatted for `destinations` parameter of Distance Matrix API

## print_matrix(api_response)
Input: Response from Distance Matrix API

Output (**To stdout**): Matrix of paths between each node (with distance and duration)

## matrix_by_time(api_response)
Input: Response from Distance Matrix API

Output: 2D list of travel time between each node

## matrix_by_distance(api_response)
Input: Response from Distance Matrix API

Output: 2D list of travel distance between each node

## find_path(addresses)
Queries the Distance Matrix API given string-formatted addresses.

Query chooses to avoid tolls
```
params = urllib.parse.urlencode(
    {
        "origins" : addresses,
        "destinations" : addresses,
        "key" : API_KEY,
        "avoid" : "tolls"
    }
)
```

Input: Address string formatted for `destinations` paramater of Distance Matrix API

Output: Response from Distance Matrix API