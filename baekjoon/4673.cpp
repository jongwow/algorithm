#include <iostream>
using namespace std;
int funcD(int n) {
	int nn = n;
	while (n) {
		nn += n % 10;
		n /= 10;
	}
	return nn;
}
int main() {
	int selfNumber[10001];
	for (int i = 0; i <= 10000; i++) {
		selfNumber[i] = i;
	}
	for (int i = 0; i <= 10000; i++) {
		if (selfNumber[i] != 0) {
			int sN = selfNumber[i];
			while (funcD(sN) <= 10000){
				sN = funcD(sN);
				if (selfNumber[sN] == 0)
					break;
				selfNumber[sN] = 0;
			}
		}
	}
	for (int i = 0; i <= 10000; i++)
		if (selfNumber[i]!=0)
			cout << selfNumber[i] << endl;
	return 0;
}