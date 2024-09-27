#include <bits/stdc++.h>

using namespace std;

int bfs(vector<vector<char>>, int n, int xi, int yi, int xj, int yj){
    vector<tuple<int,int>> directions = {{0,-1},{0,1},{1,0},{-1,0}}; //nslo
    deque<tuple<int,int,int>> q;
    q.push_front(make_tuple(xi, xj, 0));
    set<tuple<int,int>> visited;
    while(!q.empty()){
        auto [x, y, dist] = q.front();
        q.pop_front();
        if(x == xj and y == yj){
            return dist;
        }
        for(auto [dx, dy] : directions){
            int nx = x+dx;
            int ny = y+dy;
            if(0 <= nx  and nx < n and 0 <= ny and ny < n and !visited.count(make_tuple(nx,ny))){
                visited.insert(make_tuple(nx,ny));
                q.push_back(make_tuple(nx,ny,dist+1));
            }
        }
    }
    return -1;
}

bool possivel(vector<vector<char>> m, int n){
    vector<tuple<int,int>> mancha;
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if(m[i][j] == '*'){
                mancha.push_back(make_tuple(i,j));
            }
        }
    }
    for(int i = 1; i < mancha.size(); ++i){
        int xj = get<0>(mancha[i]);
        int yj = get<1>(mancha[i]);
        int xi = get<0>(mancha[i-1]);
        int yi = get<1>(mancha[i-1]);
        int dist = bfs(m, xi, yi, xj, yj);
        if(abs((xi-yi)+(xj-yj)) > dist){
            return false;
        }
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    //abs((pi-qi)+(pc-qc))
    int n;
    cin >> n;
    vector< vector<char> > m(n);
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){  
            cin >> m[i][j];
        }
    }
    bool poss = possivel(m, n);
    if(poss) cout << "S";
    else cout << "N";
}