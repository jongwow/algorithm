#include <iostream>
#include <queue>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define ll long long
#define INF 2000000001

using namespace std;

// ll path[5001][5001];
// ll cache[5001][5001];
int cache[5001][5001];
int visited[5001][5001];
int path[5001][5001];
int ks[5001];
int videoIndexes[5001];

int main()
{
    freopen("./15591.txt", "r", stdin);
    int N, Q;
    cin >> N >> Q;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cache[i][j] = INF;
        }
    }
    for (int i = 0; i < N - 1; i++)
    {
        int start, end, value;
        cin >> start >> end >> value;
        path[start - 1][end - 1] = value;
        path[end - 1][start - 1] = value;
    }
    int maxK = 0;

    for (int i = 0; i < Q; i++)
    {
        int k, videoIndex;
        cin >> k >> videoIndex;
        ks[i] = k;
        if (maxK < k)
        {
            maxK = k;
        }
        videoIndexes[i] = videoIndex - 1;
    }
    //=== start
    for (int i = 0; i < Q; i++)
    {
        int root = videoIndexes[i];
        queue<int> q;
        q.push(root);
        visited[root][root] = true;
        while (!q.empty())
        {
            int current = q.front();
            q.pop();
            for (int j = 0; j < N; j++)
            {
                if (path[current][j] != 0 && !visited[root][j])
                {
                    visited[root][j] = true;
                    cache[root][j] = min(cache[root][current], path[current][j]);
                    cache[j][root] = min(cache[root][current], path[current][j]);
                    q.push(j);
                }
            }
        }
    }

    for (int i = 0; i < Q; i++)
    {
        int k = ks[i];
        int videoIndex = videoIndexes[i];
        int count = -1;
        for (int j = 0; j < N; j++)
        {
            if (cache[videoIndex][j] >= k)
            {
                count++;
            }
        }
        cout << count << endl;
    }

    //=== end

    cout << "map" << endl;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (cache[i][j] != INF)
            {
                cout << cache[i][j] << " ";
            }
            else
            {
                cout << "X"
                     << " ";
            }
        }
        cout << endl;
    }

    return 0;
}