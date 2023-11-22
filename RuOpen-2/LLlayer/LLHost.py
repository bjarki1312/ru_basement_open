from IOLayer.IOWrapper import IOWrapper
from ModelClasses.ModelHost import ModelHost

class LLHost:

    def __init__(self):
        self.IOWrapper = IOWrapper()

    
    
    def addNewHost(self, host_info):
        """Appends a host to the file of hosts"""  
             
        data = self.getAllHosts()
        host = ModelHost(host_info["id"], host_info["name"], host_info["phone_number"])
        data.append(host)
        self.IOWrapper.StoreHostsToFile(data)
    
    def removehost(self, id):
        """Removes host with matching ID"""

        hosts_list = self.getAllHosts()
        new_hosts_list = [i for i in hosts_list if i.id != id]
        self.IOWrapper.StoreHostsToFile(new_hosts_list)

        if len(new_hosts_list) != hosts_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."
    
    
    def getAllHosts(self): 
        """Returns list of all teams"""
        
        data = self.IOWrapper.LoadHostsFromFile()
        return data
    
    
