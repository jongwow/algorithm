#include <iostream>
using namespace std;
bool isPrime[1111];
int main() {
	int tc;
	int n;
	int res = 0;
	isPrime[0] = false;
	isPrime[1] = false;
	isPrime[2] = true;
	for (int i = 2; i <= 1001; i++)
		isPrime[i] = true;
	for (int i = 2; i * i <= 1001; i++) {
		if (isPrime[i]) {
			for (int j = i * i; j <= 1001; j += i) {
				isPrime[j] = false;
			}
		}
	}
	cin >> tc;
	while (tc--) {
		cin >> n;
		if (isPrime[n])
			res++;
	}
	cout << res << endl;
}