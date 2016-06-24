import sys

"""
A module that implements the scripting capabilities of the simulated computer in the game. If it ends up the way I want
it to, it'll be a fully-functioning scripting language built in Python. Why you ask? Just to give the player some more
options. Obviously, its performance will be too restricted to be practical for anything else.
"""


class CommandProcessor(object):
    def __init__(self):
        pass

    def read(self, command):
        pass


class ScriptEditor(object):
    def __init__(self):
        pass


class ScriptProcessor(object):
    def start(self, code):
        pass


class IntrigueREPL(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        cp = CommandProcessor()
        done = False
        while not done:
            cp.read(raw_input("> "))


def extract_code(file_name):
    f = open(file_name, 'r')
    text = f.readline()
    f.close()
    return text


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    sp = ScriptProcessor()
    repl = IntrigueREPL()
    script = ""
    try:
        if sys.argv[1] != "-v":
            script = sys.argv[1]
        else:
            script = sys.argv[2]
    except IndexError:
        script = ""
    if script != "":
        script = extract_code(script)
        sp.start(script)
    else:
        repl.main()
