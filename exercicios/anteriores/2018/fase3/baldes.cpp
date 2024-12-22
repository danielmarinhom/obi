//2018 - Baldes

#include <bits/stdc++.h>

using namespace std;

void fun1(vector< vector<int> > &baldes, int p, int i){
    i--;
    baldes[i].emplace_back(p);
}

int diff(vector< vector<int> > baldes, int a, int b){
    a--;
    b--;
    int diff = 0;
    for(int i = 0; i < baldes.size(); ++i){
        for(int j = i; j < baldes.size(); ++j){
            sort(baldes[i].begin(), baldes[i].end());
            sort(baldes[j].begin(), baldes[j].end());
            int x = max(abs(baldes[j][0]-baldes[i][baldes[i].size()-1]), abs(baldes[j][baldes[j].size()-1]-baldes[i][0]));
            if(x > diff) diff = x;
        }
    }
    return diff;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    //adicionar bola de peso p ao balde i
    //maior diferenca absoluta possivel entre o peso de duas bolas dentro do intervalo

    int n,m; //baldes, operacoes
    cin >> n >> m;

    vector< vector<int> > baldes(n);
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        baldes[i].emplace_back(x);
    }

    vector< tuple<int,int,int> > operacoes(m);
    for(int i = 0; i < m; ++i){
        int l, j, k;
        cin >> l >> j >> k;
        operacoes[i] = make_tuple(l,j,k);

    }

    for(auto [t, p, i] : operacoes){
        if(t == 1) fun1(baldes, p, i);
        else if(t == 2){
            cout << diff(baldes, p, i) << endl;
        }
    }


}

//terminado errado, ajustar a logica do diff para apenas pegar o menor de todos os baldes e a diferenca com o maior