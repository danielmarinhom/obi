#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    vector<string> cartas(n);
    for(int i = 0; i < n; ++i){
        cin >> cartas[i];
    }
    deque<string> ordem;
    for(int i = n-1; i>=0; i--){
        for(int j = 0; j < cartas[i].size(); ++j){
            if(!ordem.empty()){
                string topo = ordem.back();
                ordem.pop_back();
                ordem.push_front(topo);
            }
        }
        ordem.push_front(cartas[i]);
    }
    for(int i = 0; i < n; ++i){
        cout << ordem[i] << endl;
    }
}