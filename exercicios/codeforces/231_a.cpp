#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<tuple<int,int,int>> friends;
    for(int i = 0; i < n; ++i){
        int p, v, t;
        cin >> p >> v >> t;
        friends.push_back(make_tuple(p,v,t));
    }
    int res = 0;
    for(int i = 0; i < n; ++i){
        int p = get<0>(friends[i]);
        int v = get<1>(friends[i]);
        int t = get<2>(friends[i]);
        if(p+v+t >= 2){res++;}
    }
    cout << res;
    return 0;
}

// 124ms