#include <bits/stdc++.h>
//barras
using namespace std;

int main(){
	int n;
	cin >> n;
	int h = -1;
	int lista[n];
	//preenchimento
	for(int i = 0; i < n; ++i){
		int xi; cin >> xi;
		if(xi > h){h = xi;}
		lista[i] = xi;
	}	
	int x[h][n];
	
	
	//verificacao
	for(int i = 0; i < h; ++i){
		for(int j = 0; j < n; ++j){
			if(lista[j] >= h-i){
				x[i][j] = 1;
			}else{
				x[i][j] = 0;
			}
		}
	}
	
	//4 4 2 5 3
	//exibicao
	for(int i = 0; i < h; ++i){
		for(int j = 0; j < n; ++j){
			cout << x[i][j] << " ";
		}
		cout << endl;
	}
}
