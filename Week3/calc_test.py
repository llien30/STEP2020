from op_parts import evaluate, tokenize


def test(line):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print(
            "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)
        )
