/*
#include <iostream>
#define N_SIZE 447214
#define ERR -1
#define ll long long
ll bot[N_SIZE + 1];
using namespace std;

int Answer;

void innerInitial() {
	ll cnt = 0;
	bot[0] = 0;
	for (int i = 1; i <= N_SIZE; i++) {
		cnt += (ll)i;
		bot[i] = cnt;
	}
}

int findBotIdx(ll x) {
	int s = 1;
	int e = N_SIZE;
	int m = 0;
	while (s <= e) {
		m = (s + e) / 2;
		if (bot[m] == x) {
			return m;
		}
		else if (bot[m] > x) {
			e = m - 1;
		}
		else {
			s = m + 1;
		}
	}
	//cout << x << "ÀÇ idx: " << s-1 << endl;
	return s - 1;
}
int countFunc(ll x) {
	if (x == 1)
		return 1;
	if (x < 1)
		return 0;
	ll bot_idx = findBotIdx(x);
	//cout << "bot_idx: " << bot_idx << endl;
	return bot_idx + countFunc(x - bot[bot_idx]);
}
int main(int argc, char** argv)
{
	setbuf(stdout, NULL);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T, test_case;

	 // freopen("input.txt", "r", stdin);

	innerInitial();
	cin >> T;
	for (test_case = 0; test_case < T; test_case++)
	{
		Answer = 0;
		ll x, y;
		cin >> x >> y;
		int left = findBotIdx(x);
		int right = findBotIdx(y);
		if (left == right)
			Answer = countFunc(y);
		else if (right - left > 1) {
			int st = bot[right - 1];
			for (int i = st; i <= y; i++) {
				int ci = countFunc(i);
				if (Answer < ci)
					Answer = ci;
			}
		}
		else {
			for (int i = x; i <= y; i++) {
				int ci = countFunc(i);

				if (Answer < ci)
					Answer = ci;
			}
		}
		// Print the answer to standard output(screen).
		cout << "Case #" << test_case + 1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}
*/
#include <cstdio>
#define N_SIZE 447214
#define ERR -1
#define ll long long
ll bot[N_SIZE+1];
int dp[11111];
int Answer;


int findBotIdx(ll x) {
	int s = 1;
	int e = N_SIZE;
	int m = 0;
	while (s <= e) {
		m = (s + e) / 2;
		if (bot[m] == x) {
			return m;
		}
		else if (bot[m] >x) {
			e = m - 1;
		}
		else {
			s = m + 1;
		}
	}
	return s-1;
}
int countFunc(ll x) {
	if (x < 0)
		return 0;
	if (x < 11110 && dp[x] != 0)
		return dp[x];
	ll bot_idx = findBotIdx(x);
	//cout << "bot_idx: " << bot_idx << endl;
	return bot_idx + countFunc(x - bot[bot_idx]);
}
void initial() {
	ll cnt = 0;
	bot[0] = 0;
	for (int i = 1; i <= N_SIZE; i++) {
		cnt += (ll)i;
		bot[i] = cnt;
	}
	dp[0] = 0;
	dp[1] = 1;
	for (int i = 1; i < 11110; i++) {
		dp[i] = countFunc(i);
	}
}
int main(int argc, char** argv)
{
	setbuf(stdout, NULL);
	int T, test_case;
	
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */

	 // freopen("input.txt", "r", stdin);

	initial();
	scanf("%d", &T);
	for (test_case = 0; test_case < T; test_case++)
	{
		Answer = 0;
		ll x, y;
		scanf("%lld %lld", &x, &y);
		int left = findBotIdx(x);
		int right = findBotIdx(y);
		if (left == right)
			Answer = countFunc(y);
		else if (right - left > 1) {
			int st = bot[right-1];
			for (int i = st; i <= y; i++) {
				int ci = countFunc(i);
				if (Answer < ci)
					Answer = ci;
			}
		}
		else{
			for (int i = x; i <= y; i++) {
				int ci = countFunc(i);
				
				if (Answer < ci)
					Answer = ci;
			}
		}
		 // Print the answer to standard output(screen).
		printf("Case #%d\n%d\n", test_case + 1, Answer);
	}

	return 0;//Your program should return 0 on normal termination.
}