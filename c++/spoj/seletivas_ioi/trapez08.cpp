#include <bits/stdc++.h>

using namespace std;

vector<int> trapezios(vector<pair<int,int>> &trap, int n){
    vector<int> resposta;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // colocar todos os membros da familia pendurados em um unico trapeezio, 
    //  cada um segura no maximo um peso menor ou igual a sua capacidade

    int n;
    cin >> n;
    vector<pair<int,int>> trap(n);
    for(int i = 0; i < n; ++i){
        int p, f; // peso, forca
        cin >> p >> f;
        trap.emplace_back(p,f);
    }
    vector<int> pesos(n);
    for(int i = 0; i < n; ++i){
        pesos[i] = trap[i].first + trap[i].second;
    }
    sort(pesos.begin(), pesos.end());
}
//nao finalzado