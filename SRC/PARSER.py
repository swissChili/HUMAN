import re
import inspect

stack = []

def stack_push(i):
    stack.append(i)

def stack_list():
    return " ".join(stack)

def return_string(given_string):
    return given_string

def say(i):
    print(i)

funcs = {
    r"^\s*STACK\.PUSH\s*\((.+)\)\s*$": {
        "function": stack_push,
        "recursion_level": 1
    },
    r"^\s*SAY\s*\((.+)\)\s*$": {
        "function": say,
        "recursion_level": 1
    },
    r"^\s*STACK\.LIST\s*$": {
        "function": stack_list,
        "recursion_level": 0
    },
    r"^\s*\".+\"\s*$": {
        "function": return_string,
        "recursion_level": 0
    }
}

def parse_line(id, line):
    for key in funcs:
        res = re.findall(key, line)
        print("TRYING: {}".format(funcs[key]))
        print("stack",stack)
        try:
            # inspect the signature of the function to see what
            # parameters it takes
            signature = len(inspect.signature(funcs[key]["function"]).parameters)
            if signature > 0:
                print("takes some parameters")
                if funcs[key]["recursion_level"] > 0:
                    print("attempting to recursively parse function", res[0])
                    funcs[key]["function"](parse_line(id, res[0]))
                else:
                    print("attempting to feed regex to function", res[0])
                    funcs[key]["function"](res[0])
            else:
                funcs[key]["function"]

        except IndexError:
            print("ERROR ON LINE {}: '{}' IS NOT DEFINED".format(id, line))

def parse ( program ):
    program = program.split('\n')
    for id, line in enumerate(program):
        parse_line(id, line)
