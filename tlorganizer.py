from jsonconf import load_config
from dirmon.dirmon import DirectoryMonitor
import shutil
import re

# http://www.pythoncentral.io/how-to-rename-move-a-file-in-python/
def move(src, dest):
    shutil.move(src, dest)

config_file = open('example.json')
config = load_config(config_file.read())

def added(file):
	print('Added: ' + file)
	for action in config['actions']:
		if not re.match(action['pattern'], file) == None:
			if action['action'] == 'move':
				print config['source'] + '/' + file + ' (to) ' + action['destination'] + '/' + file
				move(config['source'] + '/' + file, action['destination'] + '/' + file)

def removed(file):
	print('Removed: ' + file)

print config['scan']

if (config['scan'] == True):
	monitor = DirectoryMonitor(config['source'], config['interval']) 
	monitor.on_added = added
	monitor.on_removed = removed
	monitor.start()


#for action in config['actions']:
#	print action