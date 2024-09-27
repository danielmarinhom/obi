#include <bits/stdc++.h>

using namespace std;

vector<int> maior(vector<int> ns, int n){
    int maior = 0;
    for(int j = 0; j < n; ++j){
        if(ns[j] == 0 or ns[j] == 5){
            swap(ns[n-1], ns[j]);
            break;
        }
    }
    return ns;
}

int main(){
    int n;
    cin >> n;
    vector<int> ns(n);
    for(int i = 0; i < n; ++i){
        cin >> ns[i];
    }
    vector<int> m = maior(ns, n);
    if(m == ns){
        cout << "-1";
        return 0;
    }
    for(int i = 0; i < n; ++i){
        cout << m[i] << " ";
    }
    return 0;
}

//alguns casos funcionaram outros deu outra resposta, provavelmente se comparasse a soma dos digitos rodando for inverso e normal funcionaria