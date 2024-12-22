#include <bits/stdc++.h>

using namespace std;

int calculo(int n){
    int votos[n][n];
    for(int i = 0; i < n; ++i){
        int sum = 0;
        for(int j = 0; j < n; ++j){
            int x;
            cin >> x;
            votos[i][j] = x;
        }
    }
    int votosmax = INT_MIN;
    for(int i = 0; i < n; ++i){
        int atual = 0;
        for(int j = 0; j < n; ++j){
            atual += votos[j][i];
        }
        votosmax = max(atual, votosmax);
    }
    return votosmax;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 1;
    vector<int> respostas;

    while(true){
        cin >> n;
        if(n == 0) break;
        int x = calculo(n);
        respostas.push_back(x);
    }

    for(int i = 0; i < respostas.size(); ++i){
        cout << respostas[i] << '\n';
    }

    
}