################ Math Functions
import operator as op

def prod(numbers) -> float: # Will be math.prod in Python 3.8, but I'm in 3.7
    "The product of an iterable of numbers." 
    result = 1
    for n in numbers:
        result *= n
    return result

def dotproduct(A, B) -> float: return sum(a * b for a, b in zip(A, B))

def transpose(matrix): 
    return tuple(zip(*matrix))


def isqrt(n: int) -> int:
    "Integer square root (rounds down)."
    return int(n ** 0.5)

def ints(start: int, end: int, step: int=1) -> range:
    "The integers from start to end, inclusive: range(start, end+1)"
    return range(start, end + 1, step)

def floats(start, end, step=1.0):
    "Yield floats from start to end (inclusive), by increments of step."
    m = (1.0 if step >= 0 else -1.0)
    while start * m <= end * m:
        yield start
        start += step

operations = {'>': op.gt, '>=': op.ge, '==': op.eq,
              '<': op.lt, '<=': op.le, '!=': op.ne,
              '+': op.add, '-': op.sub, '*': op.mul, 
              '/': op.truediv, '**': op.pow}


