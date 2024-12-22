#include "bits/stdc++.h"

using namespace std;

int main(){
  int n,m;
  cin >> n >> m;
  int matriz[10][10];
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> matriz[i][j];
    }
  }
  int transposed[10][10];
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      transposed[j][i] = matriz[i][j];
    }
  }
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      cout << transposed[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}