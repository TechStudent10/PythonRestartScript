import os, sys, platform

currentFile = ""
while currentFile == "" or currentFile == None:
	currentFile = input("What is the file: ")

currentInfo = ""

def check():
	global currentFile
	global currentInfo
	file = open(currentFile, "r")
	data = file.read()
	if data != currentInfo:
		currentInfo = data
		return True
	else:
		return False
	file.close()

running = True
while running:
	try:
		fileHasChanged = check()
		if fileHasChanged:
			print(currentFile, "has changed")
			if platform.system() == "Windows":
				os.system("python " + currentFile)
			else:
				os.system("python3 " + currentFile)
	except KeyboardInterrupt:
		sys.exit()