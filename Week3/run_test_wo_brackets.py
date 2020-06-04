from op_parts_wo_brackets import tokenize, evaluate


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


def runTest() -> None:
    print("==== Test started! ====")
    test("1")
    test("12")
    test("1+2")
    test("2-1")
    test("2*3")
    test("2/3")
    test("1+2-3")
    test("1+2*3")
    test("1+2/3")
    test("1-2*4")
    test("2-3/2")
    test("2*3/5")
    test("1+2*3-2/3")
    test("1.2+2.1*2.5/5.6-3.0")
    print("==== Test finished! ====\n")


def main() -> None:
    runTest()
    while True:
        print("> ", end="")
        line = input()
        tokens = tokenize(line)
        answer = evaluate(tokens)
        print("answer = %f\n" % answer)

    return


if __name__ == "__main__":
    main()
