import os
import sys
import csv

from lib.Google_DistMatrix import Google_DistMatrix
from lib.Graph import Graph
from lib.Input import Input
from lib.Format import Format

if __name__=='__main__':
    # ===================================================================
    # =                                                                 =
    # =                 Verify commandline arguments                    =
    # =                                                                 =
    # ===================================================================
    
    # check for correct cmd line arguments ("python3 hamiltonian.py csv_file")
    argc = len(sys.argv)
    print(f"{argc=}")
    if argc == 1: # `python3 main.py`
        filename = "addresses/prospect.csv"
        db_name = "addresses/example_db.csv"
    elif argc == 2: # `python3 main.py {address_csv}`
        filename = sys.argv[1]
        db_name = "addresses/example_db.csv"
    elif argc == 3: # `python3 main.py {address_csv} {db_csv}`
        filename = sys.argv[1]
        db_name = sys.argv[2]
    else:
        print("Format: python3 main.py {address_csv} {db_csv}")
        exit(1)
    
    # if (len(sys.argv) < 2 or len(sys.argv) > 3):
    #     print("Format: python3 main.py <csv_file>")
    #     exit(1)
        
    # filename = sys.argv[1]
    # db_name = "addresses/example_db.csv"
    # if (len(sys.argv) == 3):
    #     db_name = sys.argv[2]
    


    # ===================================================================
    # =                                                                 =
    # =                      Initialise variables                       =
    # =                                                                 =
    # ===================================================================
    API_KEY = os.environ.get("DISTANCE_MATRIX_API_KEY",'') # API_KEY
    DM = Google_DistMatrix(API_KEY) # Initialise Google Distance Matrix API
    database = {} # database of addresses and users

    # key mappings
    i_name = 0
    i_zid = 1
    i_email = 2
    i_phone = 3
    i_order_beige = 4
    i_order_rose = 5
    i_order_shirt = 6
    i_order_champ = 7
    i_address = 8
    i_suburb = 9
    
    
    # ===================================================================
    # =                                                                 =
    # =                      Read input from CSV                        =
    # =                                                                 =
    # ===================================================================
    addresses_param_str,address_list = Input.retrieve_addresses(filename)
    
    print(f"{addresses_param_str=}")
        
    
    find_path_return = DM.GET_path(addresses_param_str)
    print(f"{find_path_return=}")

    if find_path_return['status'] != 'OK':
        print("Error: ", find_path_return['status'])
        exit(1)
        
    with open(db_name) as tsv:
        first_line_passed = False
        for line in csv.reader(tsv, dialect="excel-tab"):
            if not first_line_passed:
                first_line_passed = True
                continue
            print(f"{line=}")
            f_name = filename[:-4] # remove ".csv"
            suburb = f_name.split("/")[1].split("_")[0]
        
            # store only if suburb matches file called
            if line[i_suburb] != suburb:
                print(suburb)
                print(line[i_suburb])
                continue
                
            row = {}
            row["name"] = line[i_name]
            row["zid"] = line[i_zid]
            row["email"] = line[i_email]
            row["phone"] = line[i_phone]
            row["order_beige"] = line[i_order_beige]
            row["order_rose"] = line[i_order_rose]
            row["order_shirt"] = line[i_order_shirt]
            row["order_champ"] = line[i_order_champ]
            row["human_address"] = line[i_address]
            row["suburb"] = line[i_suburb]
            
            # get index of human_input
            addr_index = 0
            # print("searching for ", line[i_address])
            for a in address_list:
                if a == line[i_address]:
                    break
                addr_index += 1
                
            # if address not found, don't store
            if addr_index == len(address_list):
                # print("address not found")
                # print("addresses_list = ", addresses_list)
                # print("line[i_address] = ", line[i_address])
                continue
            # print(addr_index)
            # print(addresses_list)
            # match that with index of API response
            # print(find_path_return['destination_addresses'])
            row["API_address"] = find_path_return['destination_addresses'][addr_index]
            
            database[find_path_return['destination_addresses'][addr_index]] = row
            
            # print(row)
            
   
    print("======================= DB ======================")
    print(database)
    print("======================= ========== ======================")

    
    # ===== Creating graph G1 =====
    G1 = Graph(find_path_return["destination_addresses"]) 
    
    # ===== UNCOMMENT DEPENDING ON DISTANCE OR TIME =====
    # G1.graph = matrix_by_distance(find_path_return)
    G1.graph = DM.matrix_by_time(find_path_return)
    # ===================================================


    path,trip_time = G1.solve()
    Format.print_final_route(path, find_path_return["destination_addresses"], trip_time, database)

    print("Laters.")
