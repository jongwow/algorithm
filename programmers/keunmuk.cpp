//
// Created by Jongwoo on 2020-03-14.
//

//https://devth-preview.goorm.io/exam/53763/%EC%A3%BC-%EA%B5%AC%EB%A5%B4%EB%AF%B8-%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B3%B5%EA%B0%9C%EC%B1%84%EC%9A%A9-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/quiz/2
/*
 * 근묵자흑
 * */
/*
 * 문제를 읽고 이해한다.
 * 문제를 익숙한 용어로 재정의
 *  int num[N];
 *  그룹이 N-K+1개로 나뉨.
 *   1 2 3 4 5 6
 *  GREEDY? BFS? BACKTRACKING? DP? DIVIDE AND QUANQUER
 *  -> 그냥 탐색. 반드시 1로 수렴하기 때문에 1을 포함하는 그룹부터 시작해서 모든 그룹을 select 하면 된다.
 *  -> overflood? flood?
 *  idx = findOne으로 1의 색인 찾기. => 현재 1인 애를 찾아서 l, r을 저장.
 *  l을 기준으로 -K까지 flood, r을 기준으로 +K까지 flood. => 벽에 닿지 않는다면 K까지, 벽에 닿는다면 벽까지.
 *  위 과정을 반복
 * 어떻게 해결할지 계획
 *  func flood(arr, 선택한 idx, 방향 +-k(<=K))
 *  만약 k < K
 *      작업하고 return 1;
 *  만약 k == K:
 *      작업하고
 *      방향 계산해서 newK
 *      return 1+flood(arr, idx+=k, newK)
 *  func solve()
 *      idx = findOne
 *      ret = 0
 *      if idx - K < 0
 *          ret += flood(arr, idx, -idx)
 *      else
 *          ret += flood(arr, idx, +K)
 *      if idx + K > arr.Size() - 1
 *          ret += flood(arr, idx, arr.Size() - idx)
 *      else
 *          ret += flood(arr, idx, +K)
 *      return ret
 * 계획 검증
 * 프로그램 구현
 * 회고*/
#include <vector>
#include <iostream>

#define INF 987654321

using namespace std;

int flood(vector<int> &arr, int idx, int scope);

int N;
int K;

int solve(vector<int> &arr) {
    int ret = 0;
    int idx = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == 1) {
            idx = i;
            break;
        }
    }
    cout << "FINDONE:" << idx << endl;
    if (idx - (K - 1) < 0)
        ret += flood(arr, idx, -idx);
    else
        ret += flood(arr, idx, -(K - 1));
    if (idx + (K - 1) > N - 1)
        ret += flood(arr, idx, N - idx);
    else
        ret += flood(arr, idx, (K - 1));
    return ret;
}

/*
 *
 *  func flood(arr, 선택한 idx, 방향 +-k(<=K))
 *  만약 k < K
 *      작업하고 return 1;
 *  만약 k == K:
 *      작업하고
 *      방향 계산해서 newK
 *      return 1+flood(arr, idx+=k, newK)*/
int flood(vector<int> &arr, int idx, int scope) {
    cout << "flood(" << idx << ", " << scope << ")" << endl;
    if (idx < 0 || idx > N - 1) return 0;
    if (scope == 0) {
        arr[idx] = 1;
        return 1;
    }
    int d = scope > 0 ? 1 : -1;
    int ret = 1;
    if (scope * d < K - 1) {
        for (int i = idx; i != idx + scope + d; i += d) {
            arr[i] = 1;
        }
        return ret;
    } else {
        for (int i = idx; i != idx + scope + d; i += d) {
            arr[i] = 1;
        }
        idx = idx + scope;
        if (d < 0) {
            if (idx - (K - 1) < 0)
                ret += flood(arr, idx, -idx);
            else
                ret += flood(arr, idx, -(K - 1));
        } else {
            if (idx + (K - 1) > N - 1)
                ret += flood(arr, idx, N - idx);
            else
                ret += flood(arr, idx, (K - 1));
        }
        return ret;
    }
}

// solution(배열, 시작점, 끝점):
// 시작점부터 끝점까지 돌면서 만약에 1이 아닌 것이 있다면 누르고 ret +1
// [시작점, 끝점)
// 왼, 오 중 빈 곳에 넣어주기.
int solution(vector<int> &arr, int start, int end) {
    cout << "sol(" << start << ", " << end << ")" << endl;
    if (start == end) {
        arr[start] = 1;
        return 1;
    }
    int ret = 0;
    int d = (end - start) > 0 ? 1 : -1;
    for (int i = start; i != end && i >= 0 && i < N-1; i += d) {
        if (arr[i] != 1) {
            arr[i] = 1;
            ret = 1;
        }
    }
    if (ret == 0) {
        return ret;
    } else {
        ret += solution(arr, end, end + K * d);
        return ret;
    }
}

/*
 * 37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
 0  1  2 3  4 5 6 7 8 9   10 11 12131415 16 17 18 19 20 21 22 23 24 2526 27 28 29 30 31 32 33 3435 36
 */
int main() {
    cin >> N >> K;
    vector<int> nums;
    int t;
    int idx = 0;
    for (int i = 0; i < N; i++) {
        cin >> t;
        if (t == 1)
            idx = i;
        nums.push_back(t);
    }
    vector<int> inputArray;
    int res = INF;
    for (int j = idx - (K - 1); j <= idx + K - 1; j++) {
        inputArray.clear();
        inputArray.assign(nums.begin(), nums.end());
        res = min(res, solution(inputArray, j, j + K) + solution(inputArray, j, j - K));
        cout << "RES:" << res << endl;
        for (int i = 0; i < N; i++) {
            cout << inputArray[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
