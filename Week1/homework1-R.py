import sys
from typing import List, Tuple


def make_lower_sorted_word(word: str) -> str:
    lower_word = word.lower()
    sorted_word = "".join(sorted(list(lower_word)))
    return sorted_word


def make_sorted_dict(dictionary: List[str]) -> List[Tuple[str, str]]:
    # dog -> (dgo, dog) のリストを返す

    new_dictionary = []

    # それぞれの単語について文字をソートして新しい辞書に追加
    for word in dictionary:
        sorted_word = make_lower_sorted_word(word)
        new_dictionary.append((sorted_word, word))

    new_dictionary.sort(key=lambda x: x[0])

    return new_dictionary


def bisect(right: int, left: int, word: str, dictionary: List[Tuple[str, str]]) -> str:

    while right - left > 1:
        middle = (right + left) // 2
        mid_word = dictionary[middle][0]

        # 答えがmiddleより左側にある場合、rightをmiddleに変更
        if word < mid_word:
            right = middle

        # 答えがmiddleより右側にある場合、leftをmiddleに変更
        else:
            left = middle

    middle = (right + left) // 2
    if dictionary[middle][0] == word:
        return dictionary[middle][1]
    else:
        return "Anagram does not exist in this dictionary"


def search_anagram(word: str, dictionary: List[Tuple[str, str]]) -> str:

    first_word = dictionary[0][0]
    last_word = dictionary[-1][0]

    n_words = len(dictionary)
    sorted_word = make_lower_sorted_word(word)

    # bisectはリストの最初と最後を探すのがうまくいかないので別に確認しておく
    if sorted_word == first_word:
        anagram = dictionary[0][1]
        return anagram
    elif sorted_word == last_word:
        anagram = dictionary[-1][1]
        return anagram

    # それ以外の場合は辞書を二分探索
    anagram = bisect(n_words - 1, 0, sorted_word, dictionary)
    return anagram


def main() -> None:
    sys.setrecursionlimit(20000000)

    # 辞書の読み込み
    with open("dictionary.txt") as f:
        dictionary = [s.strip() for s in f.readlines()]

    sorted_dictionary = make_sorted_dict(dictionary)

    print("Ready to search Anagram")
    print('Enter "q" to stop this program')
    while True:
        in_word = input()
        if in_word == "q":
            return
        anagram = search_anagram(in_word, sorted_dictionary)
        print(anagram)


if __name__ == "__main__":
    main()
