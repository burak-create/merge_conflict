from functools import reduce


def multiply(*factor):
    return reduce(lambda x, y: x*y, factor)


def add(*term):
    return sum(term)


def decide_branch(decide):
    if(decide):
        return decide
    else:
        return decide
