import re
from itertools import islice, chain
from typing import Iterable, Tuple, Union
from collections import defaultdict


def error(err=RuntimeError, *args):
    raise err(*args)


############### Parsing input


def data(_input, sep: str = "\n", parser=str, test: bool = True):
    if not test:
        with open(_input) as f:
            _input = f.read()
    sections = _input.rstrip().split(sep)
    return [parser(section) for section in sections]


################ Functions on Iterables


def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def rest(sequence) -> object:
    return sequence[1:]


def first_true(iterable, pred=None, default=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true."""
    # first_true([a,b,c], default=x) --> a or b or c or x
    # first_true([a,b], fn, x) --> a if fn(a) else b if fn(b) else x
    return next(filter(pred, iterable), default)


def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)


identity = lambda x: x


def join(iterable, sep=""):
    "Join the items in iterable, converting each to a string first."
    return sep.join(map(str, iterable))


def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


def length(iterable):
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)


flatten = chain.from_iterable

################ Functional programming


def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def map2d(fn, grid):
    "Apply fn to every element in a 2-dimensional grid."
    return tuple(mapt(fn, row) for row in grid)


def repeat(n, fn, arg, *args, **kwds):
    "Repeat arg = fn(arg) n times, return arg."
    return nth(repeatedly(fn, arg, *args, **kwds), n)


def repeatedly(fn, arg, *args, **kwds):
    "Yield arg, fn(arg), fn(fn(arg)), ..."
    yield arg
    while True:
        arg = fn(arg, *args, **kwds)
        yield arg


def compose(f, g):
    "The function that computes f(g(x))."
    return lambda x: f(g(x))


def groupby(iterable, key=identity):
    "Return a dict of {key(item): [items...]} grouping all items in iterable by keys."
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return groups


def multimap(items: Iterable[Tuple]) -> dict:
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return tuple(map(int, re.findall("-?[0-9]+", text)))


def integers(text):
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r"-?\d+", text))


def atoms(text: str, ignore=r"", sep=None) -> Tuple[Union[float, int, str]]:
    "Parse text into atoms (numbers or strs), possibly ignoring a regex."
    if ignore:
        text = re.sub(ignore, "", text)
    return tuple(map(atom, text.split(sep)))


def atom(text: str) -> Union[float, int, str]:
    "Parse text into a single float or int or str."
    try:
        val = float(text)
        return round(val) if round(val) == val else val
    except ValueError:
        return text


cat = "".join
flatten = chain.from_iterable
Char = str  # Type used to indicate a single character
