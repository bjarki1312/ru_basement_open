import json
import os
from ModelClasses.ModelHost import ModelHost
class IOHosts:

    def __init__(self):
        """Constructor that sets the file name, and creates the file if it doesn't exist."""
        
        path = f"JsonData{os.sep}Host.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)

    def StoreHostsToFile(self, data): # data is a list of ModelHost objects
        """Stores the data to the file."""
        
        data_dict = []

        for i in data:
            data_dict.append({"id": i.id, "name": i.name, "phone_number": i.phone_number})
        
        with open(self.file_name, 'w') as data_stream:
            json.dump(data_dict, data_stream, indent = 4)
    
    def LoadHostsFromFile(self):
        """Loads the data from the file."""
        
        hosts_list = []
        data_stream = open(self.file_name)
        hosts = json.load(data_stream)

        for host in hosts:
            hosts_list.append(ModelHost(host["id"], host["name"], host["phone_number"]))

        return hosts_list

