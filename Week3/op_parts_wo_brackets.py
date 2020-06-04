from typing import Dict, List, Tuple, TypeVar

# Type declarations
Answer = TypeVar("Answer", int, float)
T = TypeVar("T", str, int, float)
Token = Dict[str, T]


def readNumber(line: str, index: int) -> Tuple[Token, int]:
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == ".":
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {"type": "NUMBER", "number": number}
    return token, index


def readPlus(line: str, index: int) -> Tuple[Token, int]:
    token = {"type": "PLUS"}
    return token, index + 1


def readMinus(line: str, index: int) -> Tuple[Token, int]:
    token = {"type": "MINUS"}
    return token, index + 1


def readTimes(line: str, index: int) -> Tuple[Token, int]:
    token = {"type": "TIMES"}
    return token, index + 1


def readDivision(line: str, index: int) -> Tuple[Token, int]:
    token = {"type": "DIVISION"}
    return token, index + 1


def tokenize(line: str) -> List[Token]:
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == "+":
            (token, index) = readPlus(line, index)
        elif line[index] == "-":
            (token, index) = readMinus(line, index)
        elif line[index] == "*":
            (token, index) = readTimes(line, index)
        elif line[index] == "/":
            (token, index) = readDivision(line, index)
        else:
            print("Invalid character found: " + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def eval_time_div(tokens: List[Token]) -> List[Token]:
    tokens.insert(0, {"type": "PLUS"})
    index = 1
    while index < len(tokens):
        if tokens[index]["type"] == "NUMBER":
            if tokens[index - 1]["type"] == "TIMES":
                tokens[index - 2]["number"] *= tokens[index]["number"]

            elif tokens[index - 1]["type"] == "DIVISION":
                if tokens[index]["number"] == 0:
                    print("Error : Cannot divided by 0")
                    exit(1)

                tokens[index - 2]["number"] /= tokens[index]["number"]

            elif tokens[index - 1]["type"] not in ["PLUS", "MINUS"]:
                print("Invalid syntax")
                exit(1)

        index += 1

    # Retokenize the calculated tokens
    calced_token = []

    for index in range(len(tokens)):
        t = tokens[index]
        if t["type"] == "PLUS":
            calced_token.append(t)
        elif t["type"] == "MINUS":
            calced_token.append(t)
        elif t["type"] in ["TIMES", "DIVISION"]:
            continue
        elif t["type"] == "NUMBER":
            if tokens[index - 1]["type"] in ["TIMES", "DIVISION"]:
                continue
            else:
                calced_token.append(t)

    return calced_token


def eval_plus_minus(tokens: List[Token]) -> Answer:
    answer = 0
    index = 1

    while index < len(tokens):
        if tokens[index]["type"] == "NUMBER":
            if tokens[index - 1]["type"] == "PLUS":
                answer += tokens[index]["number"]
            elif tokens[index - 1]["type"] == "MINUS":
                answer -= tokens[index]["number"]
            else:
                print("Invalid syntax")
                exit(1)
        index += 1

    return answer


def evaluate(tokens: List[Token]) -> Answer:
    tokens = eval_time_div(tokens)
    answer = eval_plus_minus(tokens)
    return answer
