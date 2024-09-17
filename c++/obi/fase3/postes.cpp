#include <bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  //1 m de altura, separados por 2 m
  //x < 50, substituido, 50 > x < 85, consertado, x > 85, normal
  int n;
  cin >> n;
  int postes[n];
  for(int i = 0; i < n; ++i){
    cin >> postes[i];
  }
  int conser = 0, subst = 0;
  for(int i = 0; i < n; ++i){
    if(postes[i] < 50){
      subst += 1;
    }else if(postes[i] >= 50 and postes[i] < 85){
      conser += 1;
    }
  }
  cout << subst << " " << conser;

}