#include <bits/stdc++.h>
//cafeteria
using namespace std;

int main(){
	int a,b,c,d;
	cin >> a >> b >> c >> d;
	
	int atual = d;
	while(c-a > atual && c-a-atual >= atual && atual%d == 0){
		atual += d;
	}
	//cout << atual;
	if(a == b){
		if(c-atual >= a && atual+a <= c){
		cout << "S";
	}else{cout << "N";}
	return 0;
	}
	if(c-atual >= a && c-atual <= b && (atual+a <= c || atual+b <= c)){
		cout << "S";
	}else{cout << "N";}
	return 0;
}
