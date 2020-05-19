import sys
from typing import List, Tuple


# 辞書の前処理
def make_sorted_dict(dictionary: List[str]) -> List[Tuple[str, str]]:
    new_dictionary = []

    # それぞれの単語について文字をソートして新しい辞書に追加
    for word in dictionary:

        # 全て小文字へ変換
        lower_word = word.lower()

        # 文字列のソート
        sorted_word = "".join(sorted(list(lower_word)))
        new_dictionary.append((sorted_word, word))

    # 辞書のソート
    # 組み込み関数のsort(Timsort)を使う(O(nlogn))
    sorted_dictionary = sorted(new_dictionary, key=lambda x: x[0])

    return sorted_dictionary


# 二分探索をする関数
def bisect(right: int, left: int, word: str, dictionary: List[Tuple[str, str]]) -> str:
    middle = (right + left) // 2
    mid_word = dictionary[middle][0]

    # 終了条件
    if right - left <= 1:
        return dictionary[middle][1]

    # 答えがmiddleより左側にある場合、rightをmiddleに変更
    elif word < mid_word:
        right = middle
        return bisect(right, left, word, dictionary)

    # 答えがmiddleより右側にある場合、leftをmiddleに変更
    else:
        left = middle
        return bisect(right, left, word, dictionary)


# Anagramを返す関数
def search_anagram(word: str, dictionary: List[Tuple[str, str]]) -> str:
    first_word = dictionary[0][0]
    last_word = dictionary[-1][0]

    # 辞書の中の単語数
    n_words = len(dictionary)
    sorted_word = "".join(sorted(list(word)))

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
    # 二分探索で再帰関数を使うので、再帰の上限をあげておく
    sys.setrecursionlimit(20000000)

    # 辞書の読み込み
    with open("dictionary.txt") as f:
        dictionary = [s.strip() for s in f.readlines()]

    # 辞書をソート
    sorted_dictionary = make_sorted_dict(dictionary)

    # 'q'という入力が入るまで、アナグラムを返し続ける
    while True:
        in_word = input().lower()
        if in_word == "q":
            return
        anagram = search_anagram(in_word, sorted_dictionary)
        print(anagram)


if __name__ == "__main__":
    main()
