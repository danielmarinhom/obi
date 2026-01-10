#include <bits/stdc++.h>

using namespace std;

int main(){
  int n, v;
  cin >> n >> v;
  int moedas[n];
  for(int i = 0; i < n; i++){
    cin >> moedas[i];
  }
  int dp[v];
  for(int i = 0; i < v; i++){
    for(int j = moedas[i]; j < n; j++){
      if(i == 0){
        dp[i] = 0;
      }else if(i >= moedas[j]){
        dp[i] = min(dp[i], dp[i - moedas[j]] + 1);
      }
    }
  }
}