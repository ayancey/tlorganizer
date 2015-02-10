import json

fi = open('example.json')
myson = fi.read()
fi.close()

config = json.loads(myson)

for thing in config:
	print thing + ' ' + str(config[thing])