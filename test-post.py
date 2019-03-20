import requests
import json

#TnFjYWFqTWpZdWFyakRncWVGZFR2MXlzS2hWRlNyZlJxd1Jrd0xTYg==
url = 'http://localhost:8000/v1/post/store-scheduler' # Set destination URL here
post_fields = {'data': [{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53718354_800784956965351_5182029169638244352_n.jpg?_nc_cat=102&_nc_ht=scontent-sin6-2.xx&oh=6d3846c2d217a90d310376d9d76f00d0&oe=5CDB327D","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53453734_800474983663015_3930341301467217920_n.jpg?_nc_cat=109&_nc_ht=scontent-sin6-2.xx&oh=1bd1f9590eb85bb8f88c5058537fc330&oe=5D153D44","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53516179_2364723256873877_138651220876197888_n.jpg?_nc_cat=107&_nc_ht=scontent-sin6-2.xx&oh=49441442544eeba99196beed0030cf38&oe=5D22EAA5","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/52608889_2795581840453756_6786281024713129984_n.jpg?_nc_cat=103&_nc_ht=scontent-sin6-2.xx&oh=7af5880b010e0f0a055e68d6364ea186&oe=5D24DF6F","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53532454_800354050341775_2333978115904110592_o.jpg?_nc_cat=106&_nc_ht=scontent-sin6-2.xx&oh=a2276af14729630a8a5a65a8dd56fd9a&oe=5D15931A","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/54278393_622586481539647_2846905379797860352_n.jpg?_nc_cat=105&_nc_ht=scontent-sin6-2.xx&oh=5e9ea7d77fedb96f8636f0036ebc66d2&oe=5CDB97A1","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53559977_800314560345724_4462986919130693632_o.jpg?_nc_cat=100&_nc_ht=scontent-sin6-2.xx&oh=c7efeed210d6b24e8fd3e458292236b2&oe=5D0EC3D7","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53472669_800265383683975_2490099459854172160_n.jpg?_nc_cat=102&_nc_ht=scontent-sin6-2.xx&oh=6f0796fbecd031001b8082bd674abd28&oe=5D190A4F","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53657238_2236323906641275_9063627840745897984_o.jpg?_nc_cat=103&_nc_ht=scontent-sin6-2.xx&oh=892920bd1741abd9079a300d0a676e11&oe=5D22E823","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53676948_2101504769933954_1108498906972422144_n.jpg?_nc_cat=106&_nc_ht=scontent-sin6-2.xx&oh=26d3a18b41f246e42d960bd497cc018d&oe=5D075071","id":"PenahanRasaBerak"},{"img":"https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/53574763_800028143707699_7808812871311163392_n.jpg?_nc_cat=111&_nc_ht=scontent-sin6-2.xx&oh=0c2b999087fb9160fc12d6d18ce1e9b0&oe=5D0EFE04","id":"PenahanRasaBerak"}]}

headers = {'Content-Type' : 'application/json','Authorization' : 'aFA0NUFjMGN3Zk5MSVlJV3VLa0U5R3p3RFAyekFEZzN1RjVWNjFGYw=='}
# data = urlencode(post_fields).encode()
# request = Request(url,data=data)

# json = urlopen(request).read().decode()
# print(json)

r = requests.post(url, data = json.dumps(post_fields), headers =headers)

print(r.text)