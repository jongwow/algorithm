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
    queue<Vertex> bigQue;
    for(int i = 0; i < Q;  i++){
        bigQue.push((Vertex){
            videoIndex: videoIndexes[i],
            leftK: ks[i]
        });
    }
	while (!bigQue.empty()) {
		Vertex cur = bigQue.front();
		bigQue.pop();
        for(int i = 0; i < N; i++){
            if(map[cur.videoIndex][])
        }
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