#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
char lights[10][10]; 
//켜진 곳을 가운데라고 생각하고 누를 경우와 켜진 곳을 위쪽이라고 생각하고 한칸 아래를 누를 경우 상태트리를 나눠서 그 계산의 끝에 완성(모두 꺼짐)의 형태일 경우 cnt를 반환, 아닐 경우 INF 반환

//이 x,y가 누를 수 있는 위치(범위 안에 존재)하는지 확인하는 safe 함수
bool safe(int x, int y) {
	return (x >= 0 && x < 10) && (y >= 0 && y < 10);
}

//iX, iY를 눌렀을 때 lights의 값을 바꿔주는 함수. //켜져있으면 끄고, 꺼져있으면 키고
void lightOff(int iX, int iY) {
	lights[iY][iX] = (lights[iY][iX] == 'O') ? '#' : 'O';
	for (int i = 0; i < 4; i++) {
		int nX = iX + dx[i], nY = iY + dy[i];
		if (safe(nX, nY)) {
			lights[nY][nX] = (lights[nY][nX] == 'O') ? '#' : 'O';
		}
	}
}
/*
시작칸부터 종료칸 까지 하나하나 검사한다
만약에 O일 경우 (켜져있을 경우)
    처음 줄이면 두가지 경우로 나눠서 계산한다.
		1) 가운데일 경우
			해당 위치를 눌렀을 때의 cnt를 계산한다.
			해당 위치를 다시 눌러준다(꺼준다)
		2) 위쪽일 경우
			해당 위치를 눌렀을 때의 cnt를 계산한다.
			해당 위치를 다시 눌러준다(꺼준다)
		둘 중 작은 값을 res에 저장하고 어느쪽인지 확인해서 그 쪽을 다시 눌러준다.
	처음 줄이 아니면 한가지로만 계산한다.
		1) 위쪽일 경우
			해당 위치를 눌렀을 때의 cnt를 계산한다.
종료칸까지 다 검사
처음칸부터 종료칸까지 다시 검사하며 하나라도 O가 있을 경우 res=INF 대입.
res값을 반환한다.
*/
int pressBtn(int ii, int jj) {
	int cnt = INF;
	for (int i = ii; i < 10; i++) {
		for (int j = jj; j < 10; j++) {
			if (lights[i][j] == 'O') {
				if (i == 0) {
					int f = 0 , s = 0;
					lightOff(i, j);
					f = pressBtn(i, j+1);
					lightOff(i, j);
					lightOff(i + 1, j);
					s = pressBtn(i, j + 1);
					lightOff(i + 1, j);
					if (s > f) {
						cnt = min(cnt,f);
						lightOff(i, j);
					}
					else {
						cnt = min(cnt,s);
						lightOff(i + 1, j);
					}
				}
				else {
					lightOff(i + 1, j);
					cnt = min(cnt, pressBtn(i, j + 1));
				}
			}
		}
	}
	for (int i = ii; i < 10; i++) {
		for (int j = jj; j < 10; j++) {
			if (lights[i][j] == 'O') {
				if (i == 0) {
					int f = 0, s = 0;
					lightOff(i, j);
					f = pressBtn(i, j + 1);
					lightOff(i, j);
					lightOff(i + 1, j);
					s = pressBtn(i, j + 1);
					lightOff(i + 1, j);
					if (s > f) {
						cnt = min(cnt, f);
						lightOff(i, j);
					}
					else {
						cnt = min(cnt, s);
						lightOff(i + 1, j);
					}
				}
				else {
					lightOff(i + 1, j);
					cnt = min(cnt, pressBtn(i, j + 1));
				}
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (lights[i][j] == 'O')
				cnt = -1;
		}
	}
	//cout << "i,j = " << ii << ", " << jj << "//" << cnt << "\n";
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	for (int i = 0; i < 10; i++)
		cin >> lights[i];
	cout << pressBtn(0, 0) << "\n";
}