#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n, m;
  cin >> n;

  vector<int> x(n);
  for(int i = 0; i < n; i++){
    cin >> x[i];
  }
  //leitura dos m
  cin >> m;
  vector<int> y(m);
  for(int i = 0; i < m; i++){
    cin >> y[i];
  }
  
  for(auto it = x.begin(); it != x.end();){
    if(find(y.begin(), y.end(), *it) != y.end()){
      it = x.erase(it);
    } else{
      ++it;
    }
  }




}