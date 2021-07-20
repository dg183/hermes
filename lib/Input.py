
class Input:
    # def __init__(self):
    #     self.address_list = []
    # Given path to a csv file, this function will return the parameter string for destination nodes
    # for the Distance Matrix API
    @staticmethod
    def retrieve_addresses(filename):
        address_list = []
        first_line_passed = False
        with open(filename) as file: #open file
            for line in file:  # iterate through each line
                if not first_line_passed: # if first line, list will be empty, continue
                    first_line_passed = True
                    continue
                # print(line)

                line = line.rstrip() # remove whitespace
                if not line: # if empty line, continue
                    continue
                address_list.append(line) # append address to list
        
        addresses_param_str = Input._address_list_to_param_str(address_list)
        
        return addresses_param_str, address_list

        
    # Convert list of addresses to Distance Matrix API parameter string
    @staticmethod
    def _address_list_to_param_str(address_list):
        addr_str = ""
        
        for addr_line in address_list:
            words = addr_line.split(" ")
            for word in words:
                addr_str += word
                addr_str += "+"
            addr_str = addr_str[:-1]
            addr_str += "|"
            
        return addr_str

if __name__=="__main__":
    addresses_param_str,address_list = Input.retrieve_addresses("../addresses/prospect.csv")

    print("==== Addresses_str ====")
    print(addresses_param_str)

    print("==== Addresses_list ====")
    print(addresses_list)