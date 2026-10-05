import requests

# freq_data = [10,20,30,40,50]
freq_data = [20,30,40,50,'asdf']

BASE="http://127.0.0.1:5000/"

for i in range(len(freq_data)):
    response = requests.put(BASE+"sensors",{"frequency":freq_data[i]})
    print(response.json())

response = requests.patch(BASE+"sensors/1",{'status':'INIT', 'measurement':29.34})
print(response.json())

response = requests.patch(BASE+"sensors/1",{'status':'ACTIVE', 'measurement':77.64})
print(response.json())

response = requests.patch(BASE+"sensors/1",{'status':'ACTIVE', 'measurement':49.91})
print(response.json())

response = requests.patch(BASE+"sensors/2",{'status':'INIT', 'measurement':12.34})
print(response.json())

response = requests.patch(BASE+"sensors/2",{'status':'ACTIVE', 'measurement':45.34})
print(response.json())

response = requests.patch(BASE+"sensors/3",{'status':'ACTIVE', 'measurement':67.34})
print(response.json())

response = requests.patch(BASE+"sensors/4",{'status':'ACTIVE', 'measurement':95.34})
print(response.json())

response = requests.get(BASE+"sensors/1")
print(response.json())

# response = requests.get(BASE+"poll")
# print(response.json())
#
# response = requests.get(BASE+"sensors/1")
# print(response.json())