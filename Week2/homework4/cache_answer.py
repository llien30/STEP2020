from test_homework4 import cache_test
from typing import List


class Cache:
    def __init__(self, n: int) -> None:
        assert n >= 1
        self.list_head = {"url": "", "contents": "", "prev": None, "next": None}
        self.list_tail = {"url": "", "contents": "", "prev": None, "next": None}
        self.list_head["next"] = self.list_tail
        self.list_tail["prev"] = self.list_head
        self.n = n
        self.len_cache = 0
        self.url2node = {}

    def access_page(self, url: str, contents: str) -> None:
        # when the accessed page is cached
        if url in self.url2node:
            node = self.url2node[url]

            node["prev"]["next"] = node["next"]
            node["next"]["prev"] = node["prev"]

        # when the accessed page is not cached
        else:
            assert self.len_cache <= self.n
            if self.len_cache == self.n:
                delete_node = self.list_tail["prev"]
                del self.url2node[delete_node["url"]]
                delete_node["prev"]["next"] = self.list_tail
                self.list_tail["prev"] = delete_node["prev"]
                self.len_cache -= 1

            node = {"url": url, "contents": contents, "prev": None, "next": None}
            self.url2node[url] = node
            self.len_cache += 1

        node["next"] = self.list_head["next"]
        node["prev"] = self.list_head
        self.list_head["next"]["prev"] = node
        self.list_head["next"] = node

    def get_pages(self) -> List:
        node = self.list_head["next"]
        cached_url = []

        while node["next"]:
            cached_url.append(node["url"])
            node = node["next"]
        return cached_url


def main() -> None:
    test = cache_test(Cache)
    test.test()


if __name__ == "__main__":
    main()
