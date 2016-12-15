#!/usr/bin/env python

import sys

# Checking if argparse is installed
try:
	import argparse
except ImportError:
	sys.stderr.write("[Error] The python module \"argparse\" is not installed\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running \"sudo easy_install argparse\"\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency \"argparser\"")

parser = argparse.ArgumentParser(prog="template_engine.py")
parser.add_argument("name", nargs='?', help="Set the name for the script to create", default="new_script.py")
args = parser.parse_args()


def main():
	output_file = open(args.name, "w")

	output_file.write("""#!/usr/bin/env python

# Licence: 

# Usage:

import sys

try:
    import argparse
except ImportError:
	sys.stderr.write("[Error] The python module \'argparse\' is not installed\\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running \'sudo easy_install argparse\'\\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency \'argparser\'")
														        
parser = argparse.ArgumentParser(prog="ADD-SCRIPT-NAME-HERE")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

def main():
	### Remove the next line and add your own code instead ###
	print "Try \'%s -h\'" % sys.argv[0]


if __name__ == "__main__":
    main()
""")
	
	output_file.close()

	
if __name__ == "__main__":
	main()
