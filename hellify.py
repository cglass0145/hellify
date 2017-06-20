#!/usr/bin/python
# - *- coding: utf- 8 - *-
import os
import argparse

# Program takes an input file and uses Perl regex to replace all important programming characters with their homoglyphic versions
# Why am I using a Python script to run a perl command through Bash? Because fuck you, that's why.
# I'm just kidding about that last part. I'm just most familiar with Python for taking input through a CLI, so I like to use that.

# Colors because I'm fabulous. Also I straight up stole this class from stackoverflow:
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def parseArgs():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Input file) # this argument, file, will be our file input")
	args = parser.parse_args()

def main():
	print bcolors.HEADER
	parseArgs()
	if "hellify.py" in args.file:
		print "Hellifyseption?"
		print "Very well..."
	print "Hellifying "+args.file+"!"
	print bcolors.ENDC
	print bcolors.BOLD
	print "[+] Replacing all slashes...",
	os.system("perl -pi -e 's/\// ̸/g' "+args.file)
	print "done."
	print "[+] Replacing all periods...",
	os.system("perl -pi -e 's/\./․/g' "+args.file)
	print "done."
	print "[+] Replacing all commas...",
	os.system("perl -pi -e 's/\,/‚/g' "+args.file)
	print "done."
	print bcolors.ENDC
if __name__=="__main__":
	try:
		main()
	except:
		print bcolors.ENDC # So in the case of an error at least the colors are gone.