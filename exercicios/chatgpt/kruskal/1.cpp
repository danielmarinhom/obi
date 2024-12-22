#include <bits/stdc++.h>

using namespace std;

int findSet(vector<int> &parent, int x){
    if(x != parent[x]){
        parent[x] = findSet(parent, parent[x]);
    }
    return parent[x];
}

void unionSet(vector<int> &parent, int a, int b){
    int rootA = findSet(parent, a);
    int rootB = findSet(parent, b);
    if(rootA != rootB){
        if(rootA > rootB){
            parent[rootB] = rootA;
        }else{
            parent[rootA] = rootB;
        }
    }
}

int kruskal(vector<tuple<int,int,int>> edges, int n, int m){
    sort(edges.begin(), edges.end());
    vector<int> parent(n);
    for(int i = 0; i < n; ++i){
        parent[i] = i;
    }

    int mstw = 0;
    vector<tuple<int,int>> mst;
    for(auto [w,u,v] : edges){
        if(findSet(parent, u) != findSet(parent, v)){
            unionSet(parent, u, v);
            mstw += w;
            mst.emplace_back(make_tuple(u,v));
            if(mst.size() == m-1){
                break;
            }
        }
    }
    return mstw;
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m; //vertices, edges

    cin >> n >> m;

    vector< tuple<int,int,int> > edges(m);
    for(int i = 0; i < m; ++i){
        int u,v,w;
        cin >> u >> v >> w;
        u--;
        v--;
        edges[i] = make_tuple(w,u,v);
    }
    int weight = kruskal(edges, n, m);
    cout << weight;

}