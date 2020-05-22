import argparse

from collections import defaultdict
from typing import DefaultDict, List, Tuple


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dictionary", type=str, default="dictionary.txt", help="dictionary file name"
    )
    return parser.parse_args()


def make_letter2point() -> DefaultDict[str, int]:
    letter2point = defaultdict(lambda: 1)
    for letter in ["c", "f", "h", "l", "m", "p", "v", "w", "y"]:
        letter2point[letter] += 1
    for letter in ["j", "k", "q", "x", "z"]:
        letter2point[letter] += 2
    return letter2point


def make_sorted_count_dict(
    dictionary: List[str], letter2point: DefaultDict[str, int]
) -> List[Tuple[DefaultDict[str, int], int, str]]:
    # dog -> Tuple[DefaultDict{'d':1, 'g':1, 'o':1}, point ,dog]

    count_dictionary = []

    # それぞれの単語について文字数カウント,ポイント計算をして新しい辞書に追加
    for word in dictionary:

        lower_word = word.lower()
        point = 0

        # 文字数カウント,ポイント計算
        word_dict = defaultdict(int)
        for letter in lower_word:
            word_dict[letter] += 1
            point += letter2point[letter]

        # その単語にqがある時はuの個数を1減らす
        word_dict["u"] -= word_dict["q"]
        point -= letter2point["u"] * word_dict["q"]

        count_dictionary.append((word_dict, point, word))

    # ポイントが高い順に辞書をソート
    count_dictionary.sort(key=lambda x: x[1], reverse=True)

    return count_dictionary


def search_best_anagram(
    input_word: str,
    dictionary: List[Tuple[DefaultDict[str, int], str]],
    letter2point: DefaultDict[str, int],
) -> str:

    lower_input_word = list(input_word.lower())

    # 文字数カウント
    input_word_dict = defaultdict(int)
    for letter in lower_input_word:
        input_word_dict[letter] += 1

    # その単語にqがある時はuの個数を1減らす
    input_word_dict["u"] -= input_word_dict["q"]

    # 辞書内の全単語探索、一番最初に見つかったアナグラムを返す
    anagram = "Anagram does not exist in this dictionary"
    for word_dict, point, word in dictionary:
        letters = word_dict.keys()
        exists = True
        for letter in letters:
            if input_word_dict[letter] < word_dict[letter]:
                exists = False
                break

        if exists:
            anagram = word
            return anagram


def main() -> None:
    args = get_arguments()

    # 辞書の読み込み
    with open(args.dictionary) as f:
        dictionary = [s.strip() for s in f.readlines()]

    letter2point = make_letter2point()

    sorted_dict = make_sorted_count_dict(dictionary, letter2point)

    print("Ready to search Anagram")
    print('Enter "q" if you want to stop program')

    while True:
        in_word = input().lower()
        if in_word == "q":
            return
        anagram = search_best_anagram(in_word, sorted_dict, letter2point)
        print(anagram)


if __name__ == "__main__":
    main()
