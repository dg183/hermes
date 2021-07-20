from lib.Input import Input

class Format:

    # ============== Helper func for displaying time
    @staticmethod
    def display_time(seconds, granularity=2):
        intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
        )

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
    # Prints details for final trip route
    @staticmethod
    def print_final_route(path, addr_list, trip_time, database):
        
        print("==================== FINAL ROUTE =================")
        
        print("ETA = ", Format.display_time(trip_time))
        print("Number of stops = ", len(path))
        ordered_path = []
        for v in path:
            ordered_path.append(addr_list[v])
            
            API_addy = addr_list[v]
            details = database[API_addy]
            # address - name - order - mobile
            output_str = "{} - {} - Ordered[".format(API_addy,details["name"])
            
            if details["order_beige"]:
                output_str += "{} Sandy Beige hoodie - ".format(details["order_beige"])
                
            if details["order_rose"]:
                output_str += "{} Dusty Rose hoodie - ".format(details["order_rose"])
                
            if details["order_shirt"]:
                output_str += "{} Enoch Shirt - ".format(details["order_shirt"])
                
            if details["order_champ"]:
                output_str += "{} Black Champion hoodie - ".format(details["order_champ"])
                
            output_str = output_str [:-3]
            output_str += "] - {} - ({})".format(details["phone"],details["human_address"])
            # output_str += details["phone"]
            
            
            print(output_str)
                
            

        print("==================== END FINAL ROUTE =================")

        origin = addr_list[0].replace(' ','+')
        ordered_path = ordered_path[1:]
        
        print(path)

        print("==================== URL FOR ROUTE ===================")
        print("https://www.google.com/maps/dir/?api=1&origin=" + origin + "&waypoints=" + Input.address_list_to_param_straddresses_list_to_str(ordered_path)[:-1])

        print("======================================================")
