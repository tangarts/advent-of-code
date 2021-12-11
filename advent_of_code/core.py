import re
from itertools import islice, chain
from typing import Callable, Dict, Generator, Iterable, List, Tuple, Union, Sequence
from collections import defaultdict


def error(err=RuntimeError, *args) -> RuntimeError:
    raise err(*args)


# Parsing input


def data(_input, sep: str = "\n", parser=str, test: bool = True) -> List[Callable]:
    if not test:
        with open(_input) as f:
            _input = f.read()
    sections = _input.rstrip().split(sep)
    return [parser(section) for section in sections]


# Functions on Iterables


def first(iterable: Iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def rest(sequence: Sequence) -> Sequence:
    return sequence[1:]


def first_true(iterable: Iterable, pred: Callable = None, default: object = None) -> object:
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true."""
    # first_true([a,b,c], default=x) --> a or b or c or x
    # first_true([a,b], fn, x) --> a if fn(a) else b if fn(b) else x
    return next(filter(pred, iterable), default)


def nth(iterable: Iterable, n: int, default: object = None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)


def identity(x): return x


def join(iterable: Iterable, sep: str = "") -> str:
    "Join the items in iterable, converting each to a string first."
    return sep.join(map(str, iterable))


def quantify(iterable: Iterable, pred: Callable = bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


def length(iterable: Iterable) -> int:
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)


flatten = chain.from_iterable

# Functional programming


def mapt(fn: Callable, *args) -> Tuple:
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def map2d(fn: Callable, grid: Sequence[Sequence]) -> Tuple:
    "Apply fn to every element in a 2-dimensional grid."
    return tuple(mapt(fn, row) for row in grid)


def repeat(n: int, fn: Callable, arg, *args, **kwds):
    "Repeat arg = fn(arg) n times, return arg."
    return nth(repeatedly(fn, arg, *args, **kwds), n)


def repeatedly(fn, arg, *args, **kwds) -> Generator:
    "Yield arg, fn(arg), fn(fn(arg)), ..."
    yield arg
    while True:
        arg = fn(arg, *args, **kwds)
        yield arg


def compose() -> Callable:
    return identity


def compose(f: Callable) -> Callable:
    return f


def compose(f: Callable, g: Callable) -> Callable:
    "The function that computes f(g(x))."
    return lambda *x: f(g(*x))


def groupby(iterable: Iterable, key: Callable = identity) -> Dict[object, list]:
    "Return a dict of {key(item): [items...]} grouping all items in iterable by keys."
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return groups


def multimap(items: Iterable[Tuple]) -> Dict[object, list]:
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def ints(text: str) -> Tuple[int, ...]:
    "Return a tuple of all the integers in text."
    return tuple(map(int, re.findall("-?[0-9]+", text)))


def integers(text: str) -> Tuple[int, ...]:
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r"-?\d+", text))


def atoms(text: str, ignore: str=r"", sep: str = None) -> Tuple[Union[float, int, str], ...]:
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
