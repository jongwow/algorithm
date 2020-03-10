#include <iostream>
#define INF 987654321
using namespace std;
bool isPrime[100002];
bool isPartial[100002];
int partialSum1[100002];
int partialSum2[100002];
void Eratos(int n) {
	if (n <= 1) return;
	isPrime[0] = false;
	isPrime[1] = false;
	for (int i = 2; i <= n; i++) {
		isPartial[i] = false;
		isPrime[i] = true;
	}
	for (int i = 2; i*i <= n; i++) {
		if (isPrime[i]) {
			for (int j = i * i; j <= n; j += i)
				isPrime[j] = false;
		}
	}
}

void partialSummation() {
	partialSum1[0] = 0;
	partialSum2[0] = 0;
	bool flag = true;
	for (int i = 2; i <= 100000; i++) {
		if (isPrime[i]) {
			if (flag) {
				isPartial[i] = true;
				partialSum1[i] = partialSum1[i - 1] + 3 * i;
				flag = false;
			}
			else {
				partialSum1[i] = partialSum1[i - 1] - i;
				flag = true;
			}
		}
		else
			partialSum1[i] = partialSum1[i - 1];
	}
	flag = true;
	for (int i = 3; i <= 100000; i++) {
		if (isPrime[i]) {
			if (flag) {
				partialSum2[i] = partialSum2[i - 1] + 3 * i;
				flag = false;
			}
			else {
				partialSum2[i] = partialSum2[i - 1] - i;
				flag = true;
			}
		}
		else
			partialSum2[i] = partialSum2[i - 1];
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int tc;
	Eratos(100001);
	partialSummation();
	cin >> tc;
	while (tc-- > 0) {
		int a, b;
		int j = 0;
		cin >> a >> b;
		for (j = a; j <= b; j++) {
			if (isPrime[j]) {
				break;
			}
		}
		if (isPartial[j]) {
			cout << partialSum1[b] - partialSum1[a - 1] << "\n";
		}
		else {
			cout << partialSum2[b] - partialSum2[a - 1] << "\n";
		}
	}
}