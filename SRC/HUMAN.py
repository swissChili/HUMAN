import sys
import PARSER


print("WELCOME TO HUMAN, A HUMAN LANGUAGE FOR HUMANS")

if len(sys.argv) > 1:
	# do parsing
	print("LOADING FILE")
	try:
		with open(sys.argv[1], "r") as code:
			to_parse = code.read()
			code.close()
			PARSER.parse(to_parse)
	except FileNotFoundError:
		print("ERROR: FILE NOT FOUND, EXITING")
else:
	print("NO FILE SPECIFIED, PLEASE SPECIFY A FILE")