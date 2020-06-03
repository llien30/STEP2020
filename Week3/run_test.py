from op_parts import tokenize, evaluate
from calc_test import test


def runTest():
    print("==== Test started! ====")
    test("1")
    test("1+2")
    test("1.0+2.1-3")
    test("2*3")
    test("2/3")
    test("2*3/5")
    test("1+2*3")
    test("1+2/3")
    test("1+2*3-2/3")
    test("1.2+2.1*2.5/5.6-3.0")
    print("==== Test finished! ====\n")


def runBracketTest():
    print("==== Bracket Test started! ====")
    test("1.0+(2.1-3)")
    test("1.0-(2.2*3-5)")
    test("2.0*(2.5/5.0)")
    test("2.0/(2.0/3.0)")
    test("1.0*((2.5-3*4)*5)/2")
    test("(2.5*3/4-((2.0*3-4)+2)/(1.5/0.3))/4")
    print("==== Bracket Test finished! ====\n")


def main():
    runTest()
    runBracketTest()
    while True:
        print("> ", end="")
        line = input()
        tokens = tokenize(line)
        answer = evaluate(tokens)
        print("answer = %f\n" % answer)

    return


if __name__ == "__main__":
    main()
