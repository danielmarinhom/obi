#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(false);

    int maior = INT_MIN;
    for(int i = 0; i < 100; ++i){
        int n;
        cin >> n;
        if(n == 0) break;
        maior = max(n, maior);
    }
    cout << maior;
}