import sys
import json
from jsonschema import validate

sys.tracebacklimit = 0

# Accepts raw JSON
def load_config(jconfig):
	config = json.loads(jconfig)

	# Read/load schema
	file = open('schema/config.json')
	raw = file.read()
	file.close()
	schema = json.loads(raw)

	# Validate file per schema, throws big errors if it finds anything wrong
	validate(config, schema)

	if config['scan']:
		try:
			config['interval']
		except:
			raise ValueError("Interval must be specified in scan mode.")

	return config