import csv
import math
from typing import List


def index_range(page, page_size):
    '''return a tuple of size two containing a start index and an end index'''
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return the appropriate page of the dataset'''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0
        data = self.dataset()
        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
