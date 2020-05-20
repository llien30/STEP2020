import argparse

from collections import defaultdict
from typing import DefaultDict, List, Tuple


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dictionary", type=str, default="dictionary.txt", help="dictionary file name"
    )
    return parser.parse_args()


def make_count_dict(dictionary: List[str]) -> List[Tuple[DefaultDict[str, int], str]]:
    count_dictionary = []

    # それぞれの単語について文字数をカウントして新しい辞書に追加
    for word in dictionary:

        lower_word = word.lower()

        # 単語内の文字数をカウント
        word_dict = defaultdict(int)
        for letter in lower_word:
            word_dict[letter] += 1

        # その単語にqがある時はuの個数を1減らす
        word_dict["u"] -= word_dict["q"]
        count_dictionary.append((word_dict, word))

    return count_dictionary


def make_letter2point() -> DefaultDict[str, int]:
    letter2point = defaultdict(lambda: 1)
    for letter in ["c", "f", "h", "l", "m", "p", "v", "w", "y"]:
        letter2point[letter] += 1
    for letter in ["j", "k", "q", "x", "z"]:
        letter2point[letter] += 2
    return letter2point


def search_best_anagram(
    input_word: str,
    dictionary: List[Tuple[DefaultDict[str, int], str]],
    letter2point: DefaultDict[str, int],
) -> str:

    lower_input_word = list(input_word.lower())

    # 単語内の文字数をカウント
    input_word_dict = defaultdict(int)
    for letter in lower_input_word:
        input_word_dict[letter] += 1

    # その単語にqがある時はuの個数を1減らす
    input_word_dict["u"] -= input_word_dict["q"]

    # 辞書内の全単語についてAnagramかどうか確認
    # 同時に点数も計算
    max_point = 0
    for word_dict, word in dictionary:
        letters = word_dict.keys()
        exists = True
        for letter in letters:
            if input_word_dict[letter] < word_dict[letter]:
                exists = False
                break
        # Anagramだったら、点数を計算してリストに追加
        if exists:
            point = 0
            for letter in word:
                point += letter2point[letter]
            if point > max_point:
                max_point = point
                anagram = word
    return anagram


def main() -> None:
    args = get_arguments()

    # 辞書の読み込み
    with open(args.dictionary) as f:
        dictionary = [s.strip() for s in f.readlines()]

    count_dict = make_count_dict(dictionary)

    letter2point = make_letter2point()

    print("Ready to search Anagram")
    # 'q'という入力が入るまで、アナグラムを返し続ける
    # 少なくとも１回は入力があることを仮定
    while True:
        in_word = input().lower()
        if in_word == "q":
            return
        anagram = search_best_anagram(in_word, count_dict, letter2point)
        print(anagram)


if __name__ == "__main__":
    main()
