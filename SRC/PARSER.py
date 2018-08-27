import re
import inspect

stack = []

def stack_push(i):
	stack.append(i)

def stack_list():
	return " ".join(stack)

def return_string():
	return "string"

def say(i):
	print(i)
	print('SAID')

funcs = {
	r"^STACK\.PUSH\s*\((.+)\)$": stack_push,
	r"^SAY\s*\((.+)\)$": say,
	r"^STACK\.LIST\s*$": stack_list,
	r'^\s*\"(.+)\"\s*$': return_string
}

def parse_line(id, line):
	for key in funcs:
		res = re.findall(key, line)
		#print("TRYING: {}".format(funcs[key]))
		print("stack",stack)
		try:
			if len(inspect.getargspec(funcs[key]).args) == 1:
				funcs[key](parse_line(id, res[0]))
			else:
				return funcs[key]()

		except IndexError:
			print("ERROR ON LINE {}: '{}' IS NOT DEFINED".format(id, line))

def parse ( program ):
	program = program.split('\n')
	for id, line in enumerate(program):
		parse_line(id, line)
