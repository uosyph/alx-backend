#!/usr/bin/env python3
"""
Pagination for Baby Names Database

This module defines a Server class for paginating a database
of popular baby names and introduces a get_hyper function
to provide enhanced pagination functionality.
"""

import csv
import math
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

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        Retrieve enhanced pagination information for a specified page.

        Parameters:
            - page (int): The page number (1-indexed).
            - page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing pagination details:
                - page_size: the length of the returned dataset page.
                - page: the current page number.
                - data: the dataset page
                (equivalent to the return from the previous task).
                - next_page: number of the next page, None if no next page.
                - prev_page: number of the previous page,
                None if no previous page.
                - total_pages: the total number of pages in
                the dataset as an integer.
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if (page + 1) <= total_pages else None,
            "prev_page": page - 1 if (page - 1) > 0 else None,
            "total_pages": total_pages,
        }


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
