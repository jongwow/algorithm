#include <iostream>
using namespace std;

int main() {
	int e, s, m;
	int a = 1, b = 1, c = 1;
	int year = 1;
	cin >> e >> s >> m;
	//e = prevE % 15 + 1
	//s = prevS % 28 + 1
	//m = prevM % 19 + 1
	// prevE == prevS == prevM
	while (1) {
		if (a == e && b == s && c == m)
			break;
		year++;
		a++;
		b++;
		c++;
		if (a > 15) a = 1;
		if (b > 28) b = 1;
		if (c > 19) c = 1;
	}
	cout << year << endl;
	return 0;
}