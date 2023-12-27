#!/usr/bin/env python3
"""
Deletion-resilient Hypermedia Pagination

This module defines a Server class for handling pagination of a database
of popular baby names with deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Retrieve the dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve deletion-resilient hypermedia pagination details.

        Parameters:
            - index (int): The current start index of the return page.
            That is the index of the first item in the current page.
            - page_size (int): The current page size.

        Returns:
            Dict: A dictionary with the following key-value pairs:
                - index: the current start index of the return page.
                - next_index: the next index to query with. That should be the
                index of the first item after the last item on current page.
                - page_size: the current page size.
                - data: the actual page of the dataset.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= len(data)
        page_data = []
        count = 0
        next_index = None
        start = index if index else 0

        for i, item in data.items():
            if i >= start and count < page_size:
                page_data.append(item)
                count += 1
                continue
            if count == page_size:
                next_index = i
                break

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }
