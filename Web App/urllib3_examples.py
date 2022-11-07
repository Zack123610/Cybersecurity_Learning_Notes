import urllib3

# For urllib3 we need a PoolManager instance to make requests
http = urllib3.PoolManager()
url = "https://www.nostarch.com"

# Make a GET Request
response = http.request("GET", url)
print(response.data)

# With headers
headers = {'User-Agent':"Googlebot"}
response = http.request('GET', url, headers=headers)

# For POST and PUT request
# We have to encode the query parameters in the URL.
from urllib.parse import urlencode
encoded_args = urlencode({'arg':'value'})
url = 'http://httpbin.org/post?' + encoded_args
response = http.request('POST', url)
