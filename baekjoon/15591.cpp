#include <iostream>
#include <queue>
using namespace std;

int map[5001][5001];
int cache[5001][5001];
int ks[5001];
int videoIndexes[5001];

struct Vertex{
    int videoIndex, leftK;
};

int main(){
    int N, Q;
    cin >> N >> Q;
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
    queue<int> bigQue;
    for(int i = 0; i < Q;  i++){
        bigQue.push(videoIndexes[i]);
    }
   while (!bigQue.empty()) {
        int cur = bigQue.front();
        bigQue.pop();
        queue<int> smallQueue;
        for(int i = 0; i < N; i++){
            if(map[cur][i] != 0){
                smallQueue.push(i);
            }
        }
        //--
        while(!smallQueue.empty()){
            int adjOne = smallQueue.front();
            smallQueue.pop();
            if (cache[cur][adjOne] == 0){
                cache[cur][adjOne] = cache[0][cur] + map[cur][adjOne];
            }
        }
    } 
    // for(int startIndex = 0; startIndex<Q; startIndex++){
    //     int start = videoIndexes[startIndex];
    //  	while (!bigQue.empty()) {
    //         int cur = bigQue.front();
    //         bigQue.pop();
    //         queue<int> smallQueue;
    //         for(int i = 0; i < N; i++){
    //             if(map[start][i] != 0){
    //               smallQueue.push(i);
    //             }
    //         }
    //         //--
    //         while(!smallQueue.empty()){
    //             int adjOne = smallQueue.front();
    //             smallQueue.pop();
    //             if (cache[start][adjOne] == 0){
    //                 cache[start][adjOne] = cache[start][cur.videoIndex] + map[cur.videoIndex][adjOne];
    //             }
    //         }
    //     }
    // }

    }

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