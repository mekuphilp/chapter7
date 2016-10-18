import os
def run(**args):
	print "[*] In dirlister module."
	files = os.listdir(".")
	print str(files)
	return str(files) 
