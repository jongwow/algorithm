#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#define ll long long
#define INF 2000000001

using namespace std;

ll path[5001][5001];
ll cache[5001][5001];

int visited[5001];
int path[5001][5001];
int ks[5001];
int videoIndexes[5001];


int main(){
    freopen("./15591.txt", "r", stdin);
    int N, Q;
    cin >> N >> Q;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cache[i][j] = INF;
        }
    }
    for(int i = 0; i < N-1; i++){
        int start, end, value;
        cin >> start >> end >> value;
        path[start-1][end-1] = value;
        path[end-1][start-1] = value;
    }
    int maxK = 0;
    
    for(int i = 0; i < Q; i++){
        int k, videoIndex;
        cin >> k >> videoIndex;
        ks[i] = k;
        if(maxK < k){
            maxK = k;
        }
        videoIndexes[i] = videoIndex;
    }
    //=== start
    for(int i = 0; i < N; i++){
        int root = i;
        queue<int> q;
        q.push(root);
        visited[root] = true;
        while(!q.empty()){
            int current = q.front();
            q.pop();
            vector<int> adj;
            for(int near = 0; near < N; near++){
                if(path[])
                adj.push_back(near)
            }

            for(int j = 0; j < N; j++){
                if(!visited[j]){
                    if(path[current][j] != 0){
                        cache[current][j]
                    }
                }
                
            }
        }
    }
    //=== end
    cout << "map" << endl;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << path[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}