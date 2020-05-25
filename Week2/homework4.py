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


# Does your code pass all test cases? :)
def cache_test():
    # Set the size of the cache to 4.
    cache = Cache(4)
    # Initially, no page is cached.
    equal(cache.get_pages(), [])
    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # "a.com" is cached.
    equal(cache.get_pages(), ["a.com"])
    # Access "b.com".
    cache.access_page("b.com", "BBB")
    # The cache is updated to: "b.com", "a.com"
    equal(cache.get_pages(), ["b.com", "a.com"])
    # Access "c.com".
    cache.access_page("c.com", "CCC")
    # The cache is updated to: "c.com", "b.com", "a.com"
    equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
    # Access "d.com".
    cache.access_page("d.com", "DDD")
    # The cache is updated to: "d.com", "c.com", "b.com", "a.com"
    equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
    # Access "d.com" again.
    cache.access_page("d.com", "DDD")
    # The cache is updated to: "d.com", "c.com", "b.com", "a.com"
    equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
    # Access "a.com" again.
    cache.access_page("a.com", "AAA")
    # The cache is updated to: "a.com", "d.com", "c.com", "b.com"
    equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
    cache.access_page("c.com", "CCC")
    equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
    cache.access_page("a.com", "AAA")
    equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
    cache.access_page("a.com", "AAA")
    equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is full, so we need to remove the least recently accessed page "b.com".
    # The cache is updated to: "e.com", "a.com", "c.com", "d.com"
    equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
    # Access "f.com".
    cache.access_page("f.com", "FFF")
    # The cache is full, so we need to remove the least recently accessed page "c.com".
    # The cache is updated to: "f.com", "e.com", "a.com", "c.com"
    equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
    print("OK!")


# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
    assert list1 == list2
    for i in range(len(list1)):
        assert list1[i] == list2[i]


if __name__ == "__main__":
    cache_test()
