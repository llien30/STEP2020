#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <time.h>

int main(int argc, char *argv[])
{
    int n;
    n = atoi(argv[1]);

    int i;
    int j;
    int k;

    std::vector<std::vector<double>> a(n, std::vector<double>(n));
    std::vector<std::vector<double>> b(n, std::vector<double>(n));
    std::vector<std::vector<double>> c(n, std::vector<double>(n));

    // Initialize the matrices to some values.
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            a[i][j] = i * n + j; // A[i][j]
            b[i][j] = j * n + i; // B[i][j]
            c[i][j] = 0;         // C[i][j]
        }
    }

    clock_t start = clock();
    for (k = 0; k < n; k++)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    clock_t end = clock();

    const double time = static_cast<double>(end - start) / CLOCKS_PER_SEC * 1000.0;
    printf("time %lf[ms]\n", time);

    return 0;
}