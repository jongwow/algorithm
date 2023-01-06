#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#define ll long long
#define INF 2000000001

using namespace std;

ll map[5001][5001];
int path[5001][5001];
int ks[5001];
int videoIndexes[5001];

struct Vertex{
    int videoIndex, leftK;
};

int main(){
    freopen("./15591.txt", "r", stdin);
    int N, Q;
    cin >> N >> Q;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            map[i][j] = INF;
        }
    }
    for(int i = 0; i < N-1; i++){
        int start, end, value;
        cin >> start >> end >> value;
        map[start-1][end-1] = value;
        map[end-1][start-1] = value;
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
        map[i][i] = 0;
    }
    for(int k = 0; k < N; k++){
        for(int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
                path[i][j] = k;
            }
        }
    }

    // for(int i = 0; i< Q; i++){
    //     int count = 0;
    //     for(int j = 0; j < N-1; j++){
    //         if( (map[videoIndexes[i]][j] != 0) && map[videoIndexes[i]][j] < ks[i]){
    //             count++;
    //         }
    //     }
    //     cout << count << endl;
    // }
    //=== end
    cout << "map" << endl;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << map[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}