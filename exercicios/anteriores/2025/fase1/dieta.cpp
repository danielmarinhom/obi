#include <bits/stdc++.h>

using namespace std;

int main(){
	int n, m;
	cin >> n >> m;
	int atual = 0;
	for(int i = 0; i < n; ++i){
		int p, g, c;
		cin >> p >> g >> c;
		atual += (p*4) + (g*9) + (c*4);
	}
	int res = m - atual;
	if(res > 0){
		cout << res;
	}else{
		cout << "0";
	}
	return 0;
}
