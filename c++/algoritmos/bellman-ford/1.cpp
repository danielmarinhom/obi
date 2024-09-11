#include <bits/stdc++.h>

using namespace std;

 //bellman(int n, int matriz){

//}

int main(){
  int n, m;
  cin >> n >> m;
  int dist[n];
  for(int i = 0; i < n; i++){
    dist[i] = INT_MAX;
  }
  vector< tuple<int,int,int> > matriz;
  for(int i = 0; i < n; i++){
    int u,v,w;
    cin >> u >> v >> w;
    matriz.push_back(make_tuple(u,v,w));
  }


  for(int i = 0; i < n-1; i++){
    int u,v,w;
    u = get<0>(matriz[i]);
    v = get<1>(matriz[i]);
    w = get<2>(matriz[i]);
    if(dist[u] != INT_MAX and dist[u] + w < dist[v]){
      dist[v] = dist[u] + w;
    }
  }

  cout << dist[4];
}