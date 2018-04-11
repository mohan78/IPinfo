#This program takes list of IP addresses and returns a dictionary of information such as ASN,hostname,Geolocation related to supplied IP address

import requests
locdetails = {} #dictionary for storing result
def Ipcheck(args): 
  for ips in args:
    ip = ips
    link = 'http://ipinfo.io/'+ip
    info = requests.get(link).json() #API call
    locdetails[ip] = info
    for key,value in info.items():
      print(key,':',value)
  return locdetails #returns the details in a nested dictionary format
  
myips = ['10.59.202.89', '10.59.202.84'] #test input list
result = Ipcheck(myips) #Calling the function
print(result)
