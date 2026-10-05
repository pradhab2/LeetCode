import requests

BASE = "http://127.0.0.1:5000/"

data=[{"name":"First video","likes":23,"views":645},
	  {"name":"Indian Receipe","likes":213,"views":7845},
	  {"name":"Funny kids video","likes":523,"views":945},
	  {"name":"Sing2 movie","likes":43,"views":895}]

for i,rec in enumerate(data):
	print("URL is:",BASE + "video/"+str(i))
	response = requests.put(BASE + "video/"+str(i), rec)
	print(response.json())


response = requests.patch(BASE + "video/2", {"likes":545})
print(response.json())


response = requests.delete(BASE + "video/2")
print(response.json())

