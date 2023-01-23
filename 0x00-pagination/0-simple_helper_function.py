#!/usr/bin/env python3
from typing import Tuple
"""0. Simple helper function"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a function named index_range that takes
    two integer arguments page and page_size.

    The function should return a tuple of size two containing a
    start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """

    # start = (page - 1) * page_size
    # end = page * page_size
    # end = start + page_size

    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
