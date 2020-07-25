# hermes

Optimal route finder for multiple stops using the Google Maps API

To run:
`python3 hamiltonian.py addresses.csv`

# TODO

* ~~Get API key~~
* ~~Read input of addresses (probably CSV file)~~
    * ~~Multiple CSV files, separated by suburb~~
    * ~~CSV files should be passed in as a command line argument~~
* ~~Parse input to fit api call~~
* ~~Process API response to create 2d weighted graph (distances and locations from API response)~~
* Find Hamiltonian circuit of each suburb
    * Put hamiltonian functions in separate file?
* Check results by hand


# Notes
### API time complexity
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

Single CSV |  | Separated by suburb
--- | --- |---
`O(n^2)` | | `O(5*(n/5)^2) = O(n^2/5)`

For 100 addresses,
Single CSV |  | Separated by suburb
--- | --- |---
`O(100^2) = O(10,000)` | | `O(100^2/5) = O(2,000)`

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
