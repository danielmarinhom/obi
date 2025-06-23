#include <bits/stdc++.h>
//festa
using namespace std;

int main(){
	
	int e,s,l;
	vector<int> dist(3);
	cin >> e >> s >> l;
	dist[0] = e; dist[1] = s; dist[2] = l;
	int atual = dist[1];
	int passos = 0;
	for(int i = 0 ; i < 3; ++i){
		for(int j = 1; j < 3; ++j){
			for(int k = 2; k < 3; ++k){
				passos += dist[i] + dist[i]-dist[j] + abs(dist[i]-dist[j])-dist[k];
				//cout << passos << " ";
			}
		}
		if(abs(passos) < atual){atual = abs(passos);}
		passos = 0;
	}		
	cout << atual;
	return 0;
}
