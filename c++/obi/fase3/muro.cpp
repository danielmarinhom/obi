#include <bits/stdc++.h>

using namespace std;

int n;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    int um = n*n;
    int tres = n*n%3;
    

    int res = um+tres;
    

    
    cout << res;
}