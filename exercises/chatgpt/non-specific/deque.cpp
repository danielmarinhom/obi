#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    deque<string> q;

    for(int i = 0; i < n; ++i){
        string operacao;
        cin >> operacao;
        if(operacao == "add_front"){ string x; cin >> x; q.push_front(x);}
        else if(operacao == "add_back"){ string x; cin >> x; q.push_back(x);}
        else if(operacao == "remove_front"){ if(!q.empty()) q.pop_front(); else cout << "Lista vazia" << endl; }
        else if(operacao == "remove_back"){ if(!q.empty()) q.pop_back(); else cout << "Lista vazia" << endl; }
        else if(operacao == "list"){ if(q.empty()){ cout << "Lista vazia" << endl; continue;} else{ for(int i = 0; i < q.size(); ++i) cout << q[i] << endl;}}
    }
}