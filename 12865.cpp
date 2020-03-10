#/*include <iostream>
#include <stdlib.h>
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

using namespace std;
int N, K, W, V;
int dp[101][100001];
int weights[101];
int values[101];

int maxi(int a, int b) {
	return (a > b) ? a : b;
}

int packaging(int idx, int weight) {
	if (idx == N)
		return 0;
	int& ret = dp[idx][weight];
	if (ret != -1)
		return ret;
	ret = packaging(idx + 1, weight);
	if(weight + weights[idx] <= K)
		ret = MAX(ret, packaging(idx + 1, weight + weights[idx]) + values[idx]);
	return ret;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> weights[i] >> values[i];
	cout << packaging(0, 0);
	return 0;
}
*/
#include <stdio.h>
int n, k, w, v, d[100001];
int main() {
	scanf("%d %d", &n, &k);
	while (n--) {
		scanf("%d %d", &w, &v);
		for (int j = k; j >= w; j--) if (d[j - w] + v > d[j]) d[j] = d[j - w] + v;
	}
	printf("%d\n", d[k]);
	return 0;
}
/*
#include <stdio.h>
int n,k,v,w,d[100001];
int main() {
	scanf("%d%d",&n,&k);
	for(int i=0; i<n; i++) {
		scanf("%d%d",&w,&v);
		for(int j=k; j>=w; j--) if(d[j-w]+v > d[j]) d[j]=d[j-w]+v;

		//j라는 변수는 버틸 수 있는 무게(k)부터 방금 막 입력받은 물건의 무게(w)까지 j를 줄여간다
		// 줄여가면서 만약 d[j-w]+v의 값이 d[j]보다 크다면 d[j] = d[j-w]+v;
		현재 입력 받은 물건을 포함한 가치가 포함하지 않은 것보다 더 크다면 그것으로 갱신해준다.

	}
	printf("%d", d[k]);
	return 0;
}
*/