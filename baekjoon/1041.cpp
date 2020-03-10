#include <iostream>
using namespace std;
long a[6];
int main() {
	long N;
	cin >> N;
	for (long i = 0; i < 6; i++) {
		cin >> a[i];
	}
	long c1=51, c2=101, c3=151;//1¸é, 2¸é, 3¸é
	for (long i = 0; i < 6; i++) {
		if (c1 > a[i])
			c1 = a[i];
	}
	for (long i = 0; i < 5; i++) {
		for (long j = i+1; j < 6; j++) {
			if (i + j == 5)
				continue;
			if (a[i] + a[j] < c2)
				c2 = a[i] + a[j];
		}
	}

	if (c3 > a[0] + a[1] + a[2])
		c3 = a[0] + a[1] + a[2];
	if (c3 > a[0] + a[1] + a[3])
		c3 = a[0] + a[1] + a[3];
	if (c3 > a[0] + a[2] + a[4])
		c3 = a[0] + a[2] + a[4];
	if (c3 > a[0] + a[3] + a[4])
		c3 = a[0] + a[3] + a[4];

	if (c3 > a[5] + a[1] + a[2])
		c3 = a[5] + a[1] + a[2];
	if (c3 > a[5] + a[1] + a[3])
		c3 = a[5] + a[1] + a[3];
	if (c3 > a[5] + a[2] + a[4])
		c3 = a[5] + a[2] + a[4];
	if (c3 > a[5] + a[3] + a[4])
		c3 = a[5] + a[3] + a[4];

	if (N == 1) {
		long sum = 0;
		long mx = -1;
		for (long i = 0; i < 6; i++) {
			if (mx < a[i])
				mx = a[i];
			sum += a[i];
		}
		sum -= mx;
		cout << sum << endl;
	}
	else {
		long resC1 = (N - 2) * (N - 2) + 4 * (N - 2) * (N - 1);
		long resC2 = 4 * (N - 2) + 4 * (N - 1);
		long resC3 = 4;
		/*cout << "1: " << resC1 << ", 2: " << resC2 << ", 3: " << resC3 << endl;
		cout << "1: " << c1<< ", 2: " << c2<< ", 3: " << c3<< endl;*/
		long res = resC1 * c1 + resC2 * c2 + resC3 * c3;
		cout << res;
	}
	
	return 0;
}