from test_homework4 import cache_test
from typing import List


class Node:
    def __init__(self, url: str, contents: str) -> None:
        self.key = url
        self.contents = contents
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, n: int) -> None:
        self.head_ = Node("", "")
        self.tail_ = Node("", "")
        self.head_.next = self.tail_
        self.tail_.prev = self.head_
        self.max_len_ = n
        self.len_list_ = 0
        self.key2node_ = {}

    # add node next to the head
    def add(self, node: Node) -> None:
        node.next = self.head_.next
        node.prev = self.head_
        self.head_.next.prev = node
        self.head_.next = node
        self.key2node_[node.key] = node
        self.len_list_ += 1

    # remove node
    def delete(self, node: Node) -> None:
        node = self.key2node_[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.len_list_ -= 1
        del self.key2node_[node.key]

    def exists(self, key):
        if key in self.key2node_:
            return True
        else:
            return False


class Cache:
    def __init__(self, n: int) -> None:
        assert n >= 1
        self.linkedlist = LinkedList(n)

    def access_page(self, url: str, contents: str) -> None:
        # when the accessed page is cached
        if self.linkedlist.exists(url):
            node = self.linkedlist.key2node_[url]
            self.linkedlist.delete(node)

        # when the accessed page is not cached
        else:
            if self.linkedlist.len_list_ == self.linkedlist.max_len_:
                most_old_node = self.linkedlist.tail_.prev
                self.linkedlist.delete(most_old_node)

            node = Node(url, contents)

        self.linkedlist.add(node)

    def get_pages(self) -> List:
        node = self.linkedlist.head_.next
        cached_url = []

        while node.next:
            cached_url.append(node.key)
            node = node.next
        return cached_url


def main() -> None:
    test = cache_test(Cache)
    test.test()


if __name__ == "__main__":
    main()
