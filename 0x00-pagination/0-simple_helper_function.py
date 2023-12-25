#!/usr/bin/env python3
"""
Pagination Utility

This module provides a function for calculating the start and end indices
corresponding to a specified page and page size,
useful for implementing pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
        - page (int): The page number (1-indexed).
        - page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end
        indices for the specified page.
    """
    return ((page - 1) * page_size, page * page_size)
