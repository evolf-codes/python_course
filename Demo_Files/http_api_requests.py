## HTTP Request folw:
#1) DNS lookup - find the request address (takes the name and trasnlates it to IP)
#2) CLIENT makes REQUEST to IP (GET)
#3) SERVER process REQUEST
#4) SERVER issues RESPONSE --> this is RQUEST, RESPONSE CYCLE (200 OK)

#) HTTP has headers, with requests and responses
#) ACCEPT - acceptable contenst (types of data, html, json, xml)
#) RESPON status codes 2xx = sucess, 3xx = redirect, 4xx = ERROR, 5xx = SERVER ERROR

# HTTP VERBS
# GET - retrieve data, in QUERY STRING
# POST - write / send data. in REQUEST BODY
# API - application programming interface - information intended for computers to get

import requests
resp = requests.get("https://news.ycombinator.com/")
print(resp)
print(resp.ok)
#print(resp.text)


url="https://icanhazdadjoke.com/"
resp = requests.get(url)

print(f"your request to {url} came back with status code {resp.status_code}")

resp = requests.get(url,headers={"Accept":"application/json"})
data = resp.json()
print(type(data))
print(data)
print(data['joke'])


# Query String? - a way to pass data to a server to get info about request



