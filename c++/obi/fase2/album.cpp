#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x,y;
    int l1,h1, l2,h2;
    cin >> x >> y >> l1 >> h1 >> l2 >> h2;
    if(y < (h1+h2)){
        if(y < (h1+l2) and y < (l1+l2)){
            cout << "N";
            return 0;
        }
    }
    cout << "S";
    return 0;
}