#include "bits/stdc++.h"

using namespace std;

int MAX_N = 10, MAX_M = 10;

int main(){
  int n,m;
  cin >> n >> m;
  int mata[MAX_N][MAX_M], matb[MAX_N][MAX_M], matc[MAX_N][MAX_M];
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> mata[i][j];
    }
  }
    
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> matb[i][j];
    }
  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      matc[i][j] = mata[i][j] + matb[i][j];
    }
  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cout << matc[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}