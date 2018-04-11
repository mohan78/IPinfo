class IPdetails():

    global results, auth
    results = {}
    auth = 'ea0dfd4a-35ea-480e-942d-b9617f5e6dec'

    def __init__(self,args):
        self.args = args

    def printips(self):
        for ips in self.args:
            print(ips)

    def ipcheck(self):
        import json,requests
        for ips in self.args:
            link = 'https://ipfind.co/?auth='+auth+'&ip='+ips
            info = requests.get(link).json()
            results[ips] = info
        return results


            
