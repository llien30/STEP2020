from test_homework4 import cache_test
from typing import List

"""
Cache by using 'List' and 'Dict'
- Worst Time complexity : O(n)
- Space complexity : O(n)
"""


class Cache:
    def __init__(self, n: int) -> None:
        self.page_dict = {}
        self.cache_size = n
        self.cached_pages_list = []
        self.most_old = 0

    def access_page(self, url: str, contents: str) -> None:
        # when the accessed page is cached
        if url in self.page_dict:
            if len(self.cached_pages_list) < self.cache_size:
                self.cached_pages_list.remove(url)
                self.cached_pages_list.append(url)
                return

            idx = self.cached_pages_list.index(url)

            if ((idx + 1) % self.cache_size) == self.most_old:
                return

            elif idx < self.most_old:
                for i in range(idx, self.most_old + 1):
                    self.cached_pages_list[i] = self.cached_pages_list[i + 1]
                self.cached_pages_list[self.most_old] = url
                self.most_old -= 1
                self.most_old %= self.cache_size
                return

            elif idx == self.most_old:
                self.most_old += 1
                self.most_old %= self.cache_size
                return

            else:
                for i in range(idx, idx + self.cache_size):
                    if (i + 1) % self.cache_size != self.most_old:
                        self.cached_pages_list[
                            i % self.cache_size
                        ] = self.cached_pages_list[(i + 1) % self.cache_size]
                    else:
                        break
                self.cached_pages_list[self.most_old - 1] = url
                return

        # when the accessed page is not cached
        else:
            if len(self.cached_pages_list) < self.cache_size:
                self.cached_pages_list.append(url)
                self.page_dict[url] = contents
                return

            # rewrite the most old page to accessed page
            del self.page_dict[self.cached_pages_list[self.most_old]]
            self.page_dict[url] = contents
            self.cached_pages_list[self.most_old] = url
            self.most_old += 1
            self.most_old %= self.cache_size

            return

    def get_pages(self) -> List:
        cache_list = (
            self.cached_pages_list[self.most_old :]
            + self.cached_pages_list[: self.most_old]
        )
        return cache_list[::-1]


def main() -> None:
    test = cache_test(Cache)
    test.test()


if __name__ == "__main__":
    main()
