from dirmon.dirmon import DirectoryMonitor

monitor = DirectoryMonitor(".", 5)

def added(file):
	print('Added: ' + file)

def removed(file):
	print('Removed: ' + file)

monitor.on_added = added
monitor.on_removed = removed
monitor.start()