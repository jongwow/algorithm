#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
vector<vector<bool> > visited; // 0 ~ N**2-1까지 존재. x,y => x+y*N가 값이 된다.

struct Pos {
	int x, y;
};

typedef pair<Pos, Pos> plane;
bool reached(plane p, int N) {
	// cout << "call:reached" << endl;
	return (p.first.x == N - 1 && p.first.y == N - 1) || (p.second.x == N - 1 && p.second.y == N - 1);
}
int getScalarize(Pos p, int N) {
	// cout << "call:getScalarize" << endl;
	return p.x + p.y * N;
}
bool isHorizon(plane p) {
	// cout << "call:isHorizon" << endl;
	return p.first.y == p.second.y;
}
bool isVisited(plane a, int N) {
	// cout << "call:isVisited" << endl;
	return visited[getScalarize(a.first, N)][getScalarize(a.second, N)];
}
bool isSafe(plane p, vector<vector<int> > board, int N) {
	// cout << "call:isSafe" << endl;
	bool isInboundary = p.first.x >= 0 && p.first.x < N && p.first.y >= 0 && p.first.y < N && p.first.x >= 0 && p.second.x < N && p.second.y >= 0 && p.second.y < N;
	return isInboundary && (board[p.first.y][p.first.x] == 0 && board[p.second.y][p.second.x] == 0);
}
void visiting(plane p, int N) {
	// cout << "call: visiting" << endl;
	visited[getScalarize(p.first, N)][getScalarize(p.second, N)] = visited[getScalarize(p.first, N)][getScalarize(p.second, N)] = true;
}
plane movePlane(plane p, int x1, int y1, int x2, int y2) {
	// cout << "call: movePlane" << endl;
	plane ret = make_pair(Pos{ p.first.x + x1, p.first.y + y1 }, Pos{ p.second.x + x2,p.second.y + y2 });
	return ret;
}
//위 아래 오른쪽 왼쪽
int fdx[4] = { 0,0,-1,1 };
int fdy[4] = { -1,1,0,0 };
int sdx[4] = { 0,0,-1,1 };
int sdy[4] = { -1,1,0,0 };


int hfdx[4] = { 0,0,1,1 };
int hfdy[4] = { -1,0,-1,0 };
int hsdx[4] = { -1,-1,0,0 };
int hsdy[4] = { 0,1,0,1 };
int hrfdx[4] = { 0,0,0,0, };
int hrfdy[4] = { 0,0,-1,1 };
int hrsdx[4] = { 0,0,0,0 };
int hrsdy[4] = { -1,1,0,0 };

int vfdx[4] = { -1,-1,0,0 }; 
int vfdy[4] = { 0,1,0,1 };
int vsdx[4] = { 0,0,1,1 };
int vsdy[4] = { -1,0,-1,0 };
int vrfdx[4] = { 0,-1,0,1 };
int vrfdy[4] = {0, 0, 0, 0};
int vrsdx[4] = { -1,0,1,0 };
int vrsdy[4] = { 0,0,0,0 };
int solution(vector<vector<int>> board) {
	int answer = 0;
	int N = board[0].size();
	// cout << N << endl;
	visited = vector<vector<bool> >(N*N, vector<bool>(N*N, false));
	queue<plane> Q;
	queue<int> depth;
	plane startPosition = make_pair(Pos{ 0,0 }, Pos{ 1,0 });
	Q.push(startPosition);
	depth.push(0);
	while (!Q.empty()) {
		plane cur = Q.front();
		int d = depth.front();
		depth.pop();
		Q.pop();
		// cout << "d:" << d << endl;
		if (reached(cur,N)) {
			answer = d;
			break;
		}
		for (int i = 0; i < 4; i++) {
			//가능성있는 위치
			plane possibleNext = movePlane(cur, fdx[i], fdy[i], sdx[i], sdy[i]);
			if (isSafe(possibleNext, board, N) && !isVisited(possibleNext,N)) {
				visiting(possibleNext,N);
				Q.push(possibleNext);
				depth.push(d + 1);
			}
		}
		if (isHorizon(cur)) {
			for (int i = 0; i < 4; i++) {
				plane pNext = movePlane(cur, hfdx[i], hfdy[i], hsdx[i], hsdy[i]);
				plane tNext = movePlane(cur, hrfdx[i], hrfdy[i], hrsdx[i], hrsdy[i]);
				if (isSafe(pNext, board, N) && isSafe(tNext, board, N) && !isVisited(pNext,N) ) {
					visiting(pNext,N);
					Q.push(pNext); depth.push(d + 1);
				}
			}
		}
		else {
			for (int i = 0; i < 4; i++) {
				plane pNext = movePlane(cur, vfdx[i], vfdy[i], vsdx[i], vsdy[i]);
				plane tNext = movePlane(cur, vrfdx[i], vrfdy[i], vrsdx[i], vrsdy[i]);
				if (isSafe(pNext, board, N) && isSafe(tNext, board, N) && !isVisited(pNext, N)) {
					visiting(pNext,N);
					Q.push(pNext); depth.push(d + 1);
				}
			}
		}
	}
	return answer;
}
int main() {
	vector<vector<int>> board({
		vector<int>({0,0,0,1,1}),
		vector<int>({0,0,0,1,0}),
		vector<int>({0,1,0,1,1}),
		vector<int>({1,1,0,0,1}),
		vector<int>({0,0,0,0,0}),
		});
	//vector<vector<int>> board({
	//	vector<int>({0,0,0,0}),
	//	vector<int>({1,1,0,0}),
	//	vector<int>({1,1,1,0}),
	//	vector<int>({1,1,1,0})
	//	});
	// cout << "start" << endl;
	int ans = solution(board);
	 cout << ans << endl;
	return 0;
}