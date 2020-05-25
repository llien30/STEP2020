import numpy as np
import pandas as pd
import time


# the result will be saved to "homework1.csv"
def main():
    n_list = [i for i in range(1, 101)]
    calc_time = []
    np_time = []
    total_sum = []

    for i in range(1, 101):
        n = i

        a = np.zeros((n, n))  # Matrix A
        b = np.zeros((n, n))  # Matrix B
        c = np.zeros((n, n))  # Matrix C

        # Initialize the matrices to some values.
        for i in range(n):
            for j in range(n):
                a[i, j] = i * n + j
                b[i, j] = j * n + i
                c[i, j] = 0

        begin = time.time()

        # Calculate C = A * B
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i, j] += a[i, k] * b[k, j]

        end = time.time()
        # print("time: %.6f sec" % (end - begin))

        calc_time.append(end - begin)

        # Calc by np.dot
        begin = time.time()

        c = np.dot(a, b)

        end = time.time()

        np_time.append(end - begin)

        # Print C for debugging.
        total = 0
        for i in range(n):
            for j in range(n):
                # print(c[i, j])
                total += c[i, j]
        # Print out the sum of all values in C.
        # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
        # print("sum: %.6f" % total)

        total_sum.append(total)

    df = pd.DataFrame(
        {"N": n_list, "time": calc_time, "numpy time": np_time, "sum": total_sum},
        columns=["N", "time", "numpy time", "sum"],
    )
    df.to_csv("./result/homework1.csv", index=None)


if __name__ == "__main__":
    main()
