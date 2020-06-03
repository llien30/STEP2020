"""
tokens structure → list of dictionary

'+' : {'type':'PLUS'}
'-' : {'type':'MINUS'}
'*' : {'type':'TIMES'}
'/' : {'type':'DIVISION'}
'(' : {'type':'BRACKET_L'}
')' : {'type':'BRACKET_R'}
number : {'type':'NUMBER', 'number':number}

eg) 1 + 2 * 3
tokens = [{'type':'NUMBER', 'number':1},
        {'type':'PLUS'},
        {'type':'NUMBER', 'number':2},
        {'type':'TIMES'},
        {'type':'NUMBER','number':3}]
"""


def readNumber(line, index):
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


def readPlus(line, index):
    token = {"type": "PLUS"}
    return token, index + 1


def readMinus(line, index):
    token = {"type": "MINUS"}
    return token, index + 1


def readTimes(line, index):
    token = {"type": "TIMES"}
    return token, index + 1


def readDivision(line, index):
    token = {"type": "DIVISION"}
    return token, index + 1


def readLeftBracket(line, index):
    token = {"type": "BRACKET_L"}
    return token, index + 1


def readRightBracket(line, index):
    token = {"type": "BRACKET_R"}
    return token, index + 1


def tokenize(line):
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
        elif line[index] == "(":
            (token, index) = readLeftBracket(line, index)
        elif line[index] == ")":
            (token, index) = readRightBracket(line, index)
        else:
            print("Invalid character found: " + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def eval_time_div(tokens):
    # return tokens only plus and minus
    tokens.insert(0, {"type": "PLUS"})
    index = 1
    calc_index = -1

    while index < len(tokens):
        if tokens[index]["type"] == "NUMBER":
            if tokens[index - 1]["type"] == "TIMES":
                tokens[calc_index]["number"] *= tokens[index]["number"]

            elif tokens[index - 1]["type"] == "DIVISION":
                tokens[calc_index]["number"] /= tokens[index]["number"]

            elif tokens[index - 1]["type"] in ["PLUS", "MINUS"]:
                calc_index = index

            else:
                print("Invalid syntax")
                exit(1)

        index += 1

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


def eval_plus_minus(tokens):
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


def eval_op(tokens):
    tokens = eval_time_div(tokens)
    answer = eval_plus_minus(tokens)
    return answer


def evaluate(tokens):
    if len(tokens) == 1:
        return tokens[0]["number"]

    if tokens[0]["type"] != "PLUS":
        tokens.insert(0, {"type": "PLUS"})

    index = 0
    last_left_bracket = -1
    right_bracket = -1
    calced_tokens = []

    # calculate from within the innermost brackets
    while index < len(tokens):

        # after calc one brackets
        if right_bracket != -1:
            calced_tokens.append(tokens[index])

        elif tokens[index]["type"] == "BRACKET_L":
            last_left_bracket = index
            calced_tokens.append(tokens[index])

        elif tokens[index]["type"] == "BRACKET_R":
            right_bracket = index
            calced_tokens = calced_tokens[:last_left_bracket]

            # calculate within the brackets
            inner_tokens = []
            for idx in range(last_left_bracket + 1, right_bracket):
                inner_tokens.append(tokens[idx])
            inner_tokens.insert(0, {"type": "PLUS"})
            val = eval_op(inner_tokens)

            calced_tokens.append({"type": "NUMBER", "number": val})

        else:
            calced_tokens.append(tokens[index])
        index += 1

    # no brackets in input tokens
    if last_left_bracket == -1:
        return eval_op(tokens)

    # return tokens that calculated most inner brackets
    else:
        return evaluate(calced_tokens)