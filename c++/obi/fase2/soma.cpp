#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n;
    vector<int> casas(n);
    for(int i = 0; i < n; ++i)
        cin >> casas[i];
    cin >> k;

    for(int i = 0; i < n; ++i){
        for(int j = 1; j < n; j++){
            if(i == j) return 0;
            if(casas[i]+casas[j] == k){
                cout << casas[i] << " " << casas[j];
                return 0;
            }
        }
    }

}