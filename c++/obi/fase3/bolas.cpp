#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

char verificar(vector<int> bolas){
    for(int i = 0; i < 8; ++i){
        if(count(bolas.begin(), bolas.end(), bolas[i]) > bolas.size()/2){
            return 'N';
        }
    }
    return 'S';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> bolas(8);
    for(int i = 0; i < 8; ++i){
        cin >> bolas[i];
    }
    sort(bolas.begin(), bolas.end());
    cout << verificar(bolas);
}

//concluido perfeitamente, chat falou que estava errado porem quebrou a cara hahaha