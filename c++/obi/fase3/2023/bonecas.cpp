#include <bits/stdc++.h>

using namespace std;

int balanceamento(int a, int b, int c){
    return pow(max({a,b,c})-min({a,b,c}), 2);
}

int menor(vector<int> &bonecas, int k, int n){
    vector<int> balanceamentos;
    sort(bonecas.begin(), bonecas.end());
    for(int i = 0; i < n-2; ++i){
        int a = bonecas[i];
        int b = bonecas[i+1];
        int c = bonecas[i+2];
        balanceamentos.push_back(balanceamento(a,b,c));
    }
    sort(balanceamentos.begin(), balanceamentos.end());
    int menor = 0;
    for(int i = 0; i < k; ++i){
        menor += balanceamentos[i];
    }
    return menor;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    //balanceamento - (a-b)**2, cada trio deveria ser = 0
    int n,k;
    cin >> n >> k;
    vector<int> bonecas(n);
    for(int i = 0; i < n; ++i){
        cin >> bonecas[i];
    }
    int m = menor(bonecas, k, n);
    cout << m << endl;
}