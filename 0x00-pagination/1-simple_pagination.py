#!/usr/bin/env python3
"""
Pagination for Baby Names Database

This module defines a Server class
for paginating a database of popular baby names.
"""

import csv
from typing import List, Tuple


class Server:
    """
    Server class to interact with a database of popular baby names
    and provide pagination functionality.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of baby names from the database.

        Parameters:
            - page (int): The page number (1-indexed).
            - page_size (int): The number of items per page.

        Returns:
            List[List]: A list of baby names for the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        [start, end] = index_range(page, page_size)
        return self.dataset()[start:end]


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
