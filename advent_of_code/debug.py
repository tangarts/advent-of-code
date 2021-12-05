import re

def trace1(f):
    "Print a trace of the input and output of a function on one line."
    def traced_f(*args):
        result = f(*args)
        print('{}({}) = {}'.format(f.__name__, ', '.join(map(str, args)), result))
        return result
    return traced_f

def grep(pattern, iterable):
    "Print lines from iterable that match pattern."
    for line in iterable:
        if re.search(pattern, line):
            print(line)
            
class Struct:
    "A structure that can have any fields defined."
    def __init__(self, **entries): self.__dict__.update(entries)
    def __repr__(self): 
        fields = ['{}={}'.format(f, self.__dict__[f]) 
                  for f in sorted(self.__dict__)]
        return 'Struct({})'.format(', '.join(fields))


