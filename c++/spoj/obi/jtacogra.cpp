#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n;
  cin >> n;

  vector<pair<int,int>> tv;
  tv.reserve(n);
  for(int i=0; i < n; i++){
    int x,y;
    cin >> x >> y;
    tv.emplace_back(x,y);
  }

  int dist = 0;
  for(int i=0; i < n; i++){
    dist += (tv[i].first) * tv[i].second;
    //-tv[i-1].first
  }
  cout << dist;
}