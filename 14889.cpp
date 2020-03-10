#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define INF 987654321
using namespace std;
int personS[20][20];
int personN;
int teamSide[20]; // 0:스타트팀. 1:링크팀
/*teaming 함수 깨끗하게 정리가능해보인다.
나중에 하자.*/
/*풀이
기본적인 풀이 방법
teamSide 배열 : teamSide[k]는 k번째 사람의 팀을 나타낸다. 
	teamSide[8] == 0일 경우, 8번째 사람은 스타트팀
	teamSide[9] == 1일 경우, 9번째 사람은 링크팀
personS 배열 : 문제에서 주는 S_ij
personN 변수 : 사람 수

teaming 함수 : k번째 사람이 팀에 넣고 스타트팀과 링크팀의 능력치 차이 값 반환.
사실 이렇게 적어놓으면 "모든 사람이 다 들어가야 스타트팀과 링크팀을 비교할 수 있지 않나"라고 생각할 수 있는데 DFS의 뽀인트 중 하나가 이런 부분
return하는 값만 잘 조정해주면 된다. 아래 함수의 흐름을 보면 이해 가능.
teaming(스타트팀인원수, 링크팀 인원수, k번째 사람)
	모든 사람을 다 팀에 넣었을 때
		RETURN |스타트팀-링크팀|
	스타트팀이 다 찼을 때 //정원 == 인원수
		링크팀에 k번째 사람을 넣는다.
		teaming(스타트팀인원수, 링크팀인원수+1, """k+1""")의 값을 계산(result)
		링크팀에 k번째 사람을 다시 뺀다.
		RETURN result
	링크팀이 다 찼을 때
		ViceVersa
	둘다 안찼을 때
		링크팀에 k번째 사람을 넣는다.
		teaming()을 계산한다. (result_1)
		링크팀에서 k번째 사람을 빼고 고대로 스타트팀에 넣는다.
		teaming()을 계산한다. (result_2)
		result = MIN(result_1, result_2)
		RETURN result.

*/
int teaming(int teamStartN, int teamLinkN, int personK) {//스타트팀의 인원수와 링크팀의 인원수와 현재 누구인지를 이용해서 차이 출력.
	if (personK == personN) { //baseCase 마지막 사람까지 다 함.
		//스타트팀과 링크팀의 능력치 계산하는 부분
		int teamStats[2] = { 0,0 };
		for (int i = 0; i < personN; i++) {
			for (int j = 0; j < personN; j++) {
				if (teamSide[i] == -1 || teamSide[j] == -1){
					cout << "ERROR\n"; //이부분 나오면 망함. 
					break;//스택오버플로우 방지
				}
				if (teamSide[i] == teamSide[j])
					teamStats[teamSide[i]] += personS[i][j];
			}
		}
		//최종 정답 반환.
		return abs(teamStats[0] - teamStats[1]);
	}
	int res = INF;
	if(teamStartN == personN/2 || teamLinkN == personN/2){ //둘중 한 팀이 만원일 때.
		if (teamStartN == personN/2) { //스타트팀 만원
			teamSide[personK] = 1;
			res = teaming(teamStartN, teamLinkN + 1, personK + 1);
		}
		if (teamLinkN== personN / 2) { //링크팀 만원
			teamSide[personK] = 0;
			res = teaming(teamStartN+1, teamLinkN, personK + 1);
		}
		teamSide[personK] = -1;
		return res;
	}
	else { //둘다 가능할 때
		teamSide[personK] = 0;
		res = teaming(teamStartN + 1, teamLinkN, personK + 1);
		teamSide[personK] = 1;
		res = min(res, teaming(teamStartN, teamLinkN + 1, personK + 1));
		return res;
	}
}

int main() {
	cin >> personN;
	for (int i = 0; i < personN; i++) {
		for (int j = 0; j < personN; j++) {
			cin >> personS[i][j];
		}
	}
	cout << "RESULT: " << teaming(0, 0, 0) << endl;
	return 0;
}