//2022 - Caravana

#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> camelos(n);
  for(int i = 0; i < n; i++){
    cin >> camelos[i];
  }
  int media = 0;
  for(int i = 0; i < n; i++){
    media += camelos[i];
  }
  media /= n;
  for(int i = 0; i < n; i++){
    cout << media-camelos[i] << '\n';
  }

}
//CONCLUIDO PERFEITAMENTE