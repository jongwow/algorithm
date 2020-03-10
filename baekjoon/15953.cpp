#include <iostream>
using namespace std;

int main() {
	int A[21] = { 500,300,300,200,200,200,50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10 };
	int B[31] = { 512, 256, 256, 128,128,128,128,64,64,64,64,64,64,64,64,
		32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32 };
	int tc;
	int a, b;
	int res = 0;
	cin >> tc;
	while (tc--) {
		cin >> a >> b;
		res = 0;
		a -= 1;
		b -= 1;
		if (a < 0 || a > 21)
			res += 0;
		else
			res += A[a];
		if (b < 0 || b > 31)
			res += 0;
		else
			res += B[b];
		res *= 10000;
		cout << res << endl;
	}
}