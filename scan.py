# This looks ugly
from dirmon.dirmon import DirectoryMonitor
import shutil

# http://www.pythoncentral.io/how-to-rename-move-a-file-in-python/
def move(src, dest):
    shutil.move(src, dest)

monitor = DirectoryMonitor("C:\Users\Alex\Downloads", 1)

def added(file):
	print('Added: ' + file)
	if "anime" in file:
		move("C:\Users\Alex\Downloads\\" + file, "C:\Users\Alex\Documents\\" + file)

def removed(file):
	print('Removed: ' + file)

monitor.on_added = added
monitor.on_removed = removed
monitor.start()