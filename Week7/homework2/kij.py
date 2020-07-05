import time


def main():
    N = int(input())
    A = [[0] * N for _ in range(N)]
    B = [[0] * N for _ in range(N)]
    C = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            A[i][j] = i * N + j
            B[i][j] = j * N + i

    start = time.time()

    for k in range(N):
        for i in range(N):
            for j in range(N):
                C[i][j] += A[i][k] * B[k][j]
    last = time.time()
    print(f"time : {last-start}")


if __name__ == "__main__":
    main()
