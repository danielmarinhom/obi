#include <bits/stdc++.h>

using namespace std;

int bellman(int n, vector<tuple <int,int,int> > &arestas, int s, int e){
  int dist[n];
  for(int i = 0; i < n; i++){
    dist[i] = INT_MAX;
  }
  dist[s] = 0;
  for(int i = 0; i < n-1; i++){
    for(auto [u,v,w] : arestas){
      if(dist[u] != INT_MAX and dist[u]+w < dist[v]){
        dist[v] = dist[u]+w;
      }
    }
  }
  return dist[e];
}

int main(){
  int n, m;
  cin >> n >> m;
  vector< tuple<int,int,int> > arestas;
  for(int i = 0; i < m; i++){
    int u,v,w;
    cin >> u >> v >> w;
    arestas.push_back(make_tuple(u,v,w));
  }
  int x; //quantidade de consultas
  cin >> x;
  vector<pair<int,int>> consultas(x);
  for(int i = 0; i < x; i++){
    cin >> consultas[i].first >> consultas[i].second;
  }
  for(auto [s,e] : consultas){
    int dist = bellman(n, arestas, s, e);
    if(dist != INT_MAX) cout << dist << '\n';
    else cout << "INALCANCAVEL\n";
  }
  return 1;
}