#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

bool compare(const tuple<int,int,int>& a, const tuple<int,int,int>& b){
  return get<2>(a) < get<2>(b);
}

int main(){
  int n, m, l;
  cin >> n >> m >> l;
  vector< tuple<int,int,int> > estradas;
  for(int i = 0; i < m; i++){
    int u,v,w;
    cin >> u >> v >> w;
    estradas.push_back(make_tuple(u,v,w));
  }
  int maximo = 0;
  sort(estradas.begin(), estradas.end(), compare);
  for(int i = 0; i < m; i++){
    int w = get<2>(estradas[i]);
    maximo += 1;
    l -= w;
  }
  cout << maximo << endl;
}