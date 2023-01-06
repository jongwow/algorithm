#include <iostream>
#include <queue>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define INF 2000000001

using namespace std;

int cache[5001][5001];
int visited[5001][5001];
int path[5001][5001];
int ks[5001];
int videoIndexes[5001];
vector<int> adjVectors[5001];
vector<int> results[5001];

int main()
{
    freopen("./15591.txt", "r", stdin);
    int N, Q;
    cin >> N >> Q;

    for (int i = 0; i < N - 1; i++)
    {
        int start, end, value;
        cin >> start >> end >> value;
        path[start - 1][end - 1] = value;
        adjVectors[start - 1].push_back(end - 1);
        adjVectors[end - 1].push_back(start - 1);
        path[end - 1][start - 1] = value;
    }

    for (int i = 0; i < Q; i++)
    {
        int k, videoIndex;
        cin >> k >> videoIndex;
        ks[i] = k;
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

            for (int j = 0; j < adjVectors[current].size(); j++)
            {
                int next = adjVectors[current][j];
                if (path[current][next] != 0 && !visited[root][next])
                {
                    visited[root][next] = true;
                    if (cache[root][current] == 0)
                    {
                        cache[root][current] = INF;
                    }
                    cache[root][next] = min(cache[root][current], path[current][next]);
                    q.push(next);
                }
            }
        }
    }

    for (int i = 0; i < Q; i++)
    {
        int k = ks[i];
        int videoIndex = videoIndexes[i];
        int count = 0;
        for (int j = 0; j < N; j++)
        {
            if (videoIndex != j && cache[videoIndex][j] >= k)
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
            cout << cache[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}