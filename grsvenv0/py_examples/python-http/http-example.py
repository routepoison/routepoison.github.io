import http.client

conn = http.client.HTTPSConnection("https://picoctf.com/")

conn.request("GET","/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
# 200 OK
data1 = r1.read()

conn.request("GET", "/")
r2 = conn.getresponse()
print(r2.status, r2.reason)
# 404 Not Found
data2 = r2.read()

conn.close()
