import json
from jsonschema import validate

fi = open('example.json')
myson = fi.read()
fi.close()

fi = open('schema/config.json')
schema = fi.read()
fi.close()


config = json.loads(myson)
schema = json.loads(schema)

print validate(config, schema)

for thing in config:
	print thing + ' ' + str(config[thing])