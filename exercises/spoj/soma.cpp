#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    int m[n][n];
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            cin >> m[i][j];
        }
    }

    int m2[n][n];
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            cin >> m2[i][j];
        }
    }
    
    int somada[n][n];
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            somada[i][j] = m[i][j] + m2[i][j];
        }
    }

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            cout << somada[i][j] << " ";
        }
        cout << "\n";
    }

}