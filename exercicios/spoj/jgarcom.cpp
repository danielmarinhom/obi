#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n;
  vector<pair<int, int>> lc;

  cin >> n;
  for(int i = 0; i < n; i++){
    int x, y;
    cin >> x >> y;
    lc.emplace_back(x,y);
  }
  int result = 0;

  //verificando l[i] < c[i]
  for(int i = 0; i < n; i++){
    if(lc[i].first > lc[i].second){
      result += lc[i].second;
    }
  }
  cout << result;
}