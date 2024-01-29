#!/usr/bin/env python3
'''
a function named index_range that takes two integer arguments page & page_size
'''
from typing import Tuple


def index_range(page, page_size):
    '''return a tuple of size two containing a start index and an end index'''
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)
