#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;

    deque<string> q;

    vector<tuple<vector<string>>> res;
    for(int i = 0; i < n; ++i){
        string op; cin >> op;
        if(op == "add_car"){
            string x; cin >> x;
            q.push_back(x);
        }else if(op == "remove_car") if(!q.empty()) q.pop_front(); else cout << "Estacionamento Vazio" << endl;
        else if(op == "list_cars"){
            if(q.empty()){
                q.push_back({"Estacionamento Vazio"});
                continue;
            }
            vector<string> actual;
            
            for(int i = 0; i < q.size(); ++i){
                actual.push_back(q[i]);
            }
            res.push_back(make_tuple(actual));
        }
        
    }
    for(const auto& item : res) {
        const auto& cars = get<0>(item);
        cout << "Carros: ";
        for(const auto& car : cars) {
            cout << car << " ";
        }
        cout << endl;
    }
}