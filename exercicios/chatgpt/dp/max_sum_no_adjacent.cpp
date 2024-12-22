#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  int numeros[n], dp[n];
  memset(dp, 0, sizeof(dp));
  dp[0] = numeros[0];
  dp[1] = max(numeros[0], numeros[1]);
  for(int i = 0; i < n; i++){
    cin >> numeros[i];
  }
  for(int i = 2; i < n; i++){
    dp[i] = max(dp[i-1],numeros[i]+dp[i-2]);
  }
  for(int i = 0; i < n; i++){
    cout << dp[i] << " ";
  }
}