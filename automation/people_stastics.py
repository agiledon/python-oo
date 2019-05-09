#!/usr/bin/env python

from functools import reduce


def average_height(people):
    """
    calculate average height for people
    >>> people = [{'name': 'zhangyi', 'height': 168}, {'name': 'Jack', 'height': 180}, {'name': 'bruce', 'height': 170}]
    >>> average_height(people)
    169.0
    """
    heights = map(lambda p: p['height'], filter(lambda p: p['name'] != 'Jack', people))
    heights_list = list(heights)
    if len(heights_list) > 0:
        avg = reduce(lambda x, y: x + y, heights_list) / len(heights_list)
    return avg


if __name__ == "__main__":
    import doctest

    doctest.testmod()
