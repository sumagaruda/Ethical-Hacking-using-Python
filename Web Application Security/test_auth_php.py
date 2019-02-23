import urllib2

from urllib import urlencode

data = {"username":"suma", "password":"123456789"}
data_encoded = urlencode(data)

req = urllib2.request("url", data_encoded, headers={"User-Agent":"Scanner"})

final_request = urllib2.urlopen(req)

print final_request.read()
