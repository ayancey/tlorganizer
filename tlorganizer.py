from jsonconf import load_config
from dirmon import DirectoryMonitor
import shutil
import re
from os import listdir

config_file = open('example.json')
config = load_config(config_file.read())

# http://www.pythoncentral.io/how-to-rename-move-a-file-in-python/
def move(src, dest):
    shutil.move(src, dest)

def search(file):
	for action in config['actions']:
		if not re.match(action['pattern'], file) == None:
			if action['action'] == 'move':
				print config['source'] + '/' + file + ' (move to) ' + action['destination'] + '/' + file
				move(config['source'] + '/' + file, action['destination'] + '/' + file)
			if action['action'] == 'copy':
				print config['source'] + '/' + file + ' (copy to) ' + action['destination'] + '/' + file
				shutil.copyfile(config['source'] + '/' + file, action['destination'] + '/' + file)

def added(file):
	print('Added: ' + file)
	search(file)
			

def removed(file):
	print('Removed: ' + file)

print config['scan']

if (config['scan'] == True):
	monitor = DirectoryMonitor(config['source'], config['interval']) 
	monitor.on_added = added
	monitor.on_removed = removed
	monitor.start()
else:
	print config['source']
	for file in listdir(config['source']):
		search(file)

#for action in config['actions']:
#	print action