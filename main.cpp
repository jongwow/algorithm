#include <iostream>
using namespace std;
/*
0000 ´Ù ²ö »óÅÂ
0001 ALL
0010 Â¦¼ö
#0011 Â¦¼ö+ALL => È¦¼ö
0100 È¦¼ö
#0101 È¦¼ö+ALL => Â¦¼ö
#0110 È¦¼ö+Â¦¼ö => ALL
#0111 È¦¼ö+Â¦¼ö+ALL => ´Ù ²û
1000 3k_1 (Æ¯¼ö°æ¿ì)
1001 3k_1+ALL
1010 3k_1+Â¦¼ö
#1011 3k_1+ALL+Â¦¼ö => 3k_1+È¦¼ö
1100 3k_1+È¦¼ö
#1101 3k_1+È¦¼ö+ALL => 3k_1+Â¦¼ö
#1110 3k_1+È¦¼ö+Â¦¼ö => 3k_1+ALL
#1111 3k_1+È¦¼ö+Â¦¼ö+ALL => 3k_1

*/
int main() {
	int act[4]; //µ¿ÀÛ[k]¸¦ ÇÏ´Âµ¥ °É¸®´Â ½Ã°£ :  act[k]
	int status[8]; //³ª¿Ã ¼ö ÀÖ´Â ¸ğµç °æ¿ìÀÇ ¼ö¿¡ ÇØ´çÇÏ´Â °É¸®´Â ½Ã°£.
	int n, m;
	int res = 0;
	cin >> n >> m;
	act[0] = n;
	act[1] = int(n / 2);
	act[2] = n - act[1];
	act[3] = (n + 2) / 3;
	status[0] = 0;
	status[1] = act[0];
	status[2] = act[1];
	status[3] = act[2];
	status[4] = act[3];
	status[5] = act[3] + act[0];
	status[6] = act[3] + act[1];
	status[7] = act[3] + act[2];

	if (m == 0)
		res = 1;
	else {
		if (n < 3) {
			if (n == 1)	
				if (m >= 1)
					res = 2;
			if (n == 2)
				if (m >= 2)
					res = 4;
				else if (m == 1)
					res = 3;
		}
		else {
			for (int i = 0; i < 8; i++) {
				if (m >= status[i])
					res++;
			}
		}
	}
	cout << res << endl;
	return 0;
}