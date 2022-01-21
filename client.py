import http.client

connection = http.client.HTTPConnection('host', 80)
connection.request('GET','/index.html')
response = connection.getresponse()
print(response.read())