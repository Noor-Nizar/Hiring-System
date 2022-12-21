// ID 20200603
// Noor Eldeen Nizar

#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int elements = 4;
    int size = 8;
    int weight[] = {0, 3, 4, 5, 6};
    int value[] = {0, 2, 3, 4, 1};

    int **dp = new int *[elements + 1];
    for (int i = 0; i <= elements; i++)
    {
        dp[i] = new int[size + 1];
    }

    for (int i = 0; i <= elements; i++)
    {
        for (int j = 0; j <= size; j++)
        {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
        }
    }

    for (int i = 1; i <= elements; i++)
    {
        for (int j = 1; j <= size; j++)
        {
            if (weight[i] > j)
            {
                dp[i][j] = dp[i - 1][j];
            }
            else
            {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
            }
        }
    }

    for (int i = 0; i <= elements; i++)
    {
        for (int j = 0; j <= size; j++)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    // backTrack(dp, weight, value, elements, size);
    int take = -1;
    int j = size;
    for (int i = elements; i > 0; i--)
    {
        if (dp[i][j] == dp[i - 1][j])
        {
            continue;
        }
        cout << "Element " << i << " is taken"
             << "whose value is " << value[i] << " weight " << weight[i] << endl;
        j -= weight[i];
    }
    return 0;
}
