from typing import List, NoReturn


def equal(list1: List, list2: List) -> None:
    assert list1 == list2
    for i in range(len(list1)):
        assert list1[i] == list2[i]


# Does your code pass all test cases? :)
class cache_test:
    def __init__(self, Cache) -> NoReturn:
        # Set the size of the cache to 4.
        self.cache = Cache(4)

    def test(self) -> NoReturn:
        # Initially, no page is cached.
        equal(self.cache.get_pages(), [])
        # Access "a.com".
        self.cache.access_page("a.com", "AAA")
        # "a.com" is cached.
        equal(self.cache.get_pages(), ["a.com"])
        # Access "b.com".
        self.cache.access_page("b.com", "BBB")
        # The cache is updated to: "b.com", "a.com"
        equal(self.cache.get_pages(), ["b.com", "a.com"])
        # Access "c.com".
        self.cache.access_page("c.com", "CCC")
        # The cache is updated to: "c.com", "b.com", "a.com"
        equal(self.cache.get_pages(), ["c.com", "b.com", "a.com"])
        # Access "d.com".
        self.cache.access_page("d.com", "DDD")
        # The cache is updated to: "d.com", "c.com", "b.com", "a.com"
        equal(self.cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
        # Access "d.com" again.
        self.cache.access_page("d.com", "DDD")
        # The cache is updated to: "d.com", "c.com", "b.com", "a.com"
        equal(self.cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
        # Access "a.com" again.
        self.cache.access_page("a.com", "AAA")
        # The cache is updated to: "a.com", "d.com", "c.com", "b.com"
        equal(self.cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
        self.cache.access_page("c.com", "CCC")
        equal(self.cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
        self.cache.access_page("a.com", "AAA")
        equal(self.cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
        self.cache.access_page("a.com", "AAA")
        equal(self.cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
        self.cache.access_page("e.com", "EEE")
        equal(self.cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
        self.cache.access_page("f.com", "FFF")
        equal(self.cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
        print("OK!")
