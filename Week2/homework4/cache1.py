from test_homework4 import cache_test
from typing import List

"""
Cache by using 'List' and 'Dict'
- Time complexity : O(n)
- Space complexity : O(n)
"""


class Cache:
    def __init__(self, n: int) -> None:
        self.page_dict = {}
        self.cache_size = n
        self.cached_pages_list = []

    def access_page(self, url: str, contents: str) -> None:
        # when the accessed page is cached
        if url in self.cached_pages_list:
            if len(self.cached_pages_list) < self.cache_size:
                self.cached_pages_list.remove(url)
                self.cached_pages_list.append(url)
                return

            self.cached_pages_list.remove(url)
            self.cached_pages_list = [url] + self.cached_pages_list
            return

        # when the accessed page is not cached
        else:
            if len(self.cached_pages_list) < self.cache_size:
                self.cached_pages_list = [url] + self.cached_pages_list
                self.page_dict[url] = contents
                return

            # remove the most old page
            del self.page_dict[self.cached_pages_list[-1]]
            self.cached_pages_list = self.cached_pages_list[:-1]

            # add the accessed page
            self.cached_pages_list = [url] + self.cached_pages_list
            self.page_dict[url] = contents
            return

    def get_pages(self) -> List:
        return self.cached_pages_list


def main() -> None:
    test = cache_test(Cache)
    test.test()


if __name__ == "__main__":
    main()
