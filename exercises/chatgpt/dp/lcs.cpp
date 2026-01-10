#include <bits/stdc++.h>

using namespace std;

int main(){
  string x, y;
  cin >> x >> y;
  int tmx = x.size(), tmy = y.size();
  int dp[tmx][tmy];
  memset(dp, 0, sizeof(dp));
  for(int i = 1; i < tmx; i++){
    for(int j = 1; j < tmy; j++){
      if(x[i-1] == y[j-1]){
        dp[i][j] = dp[i-1][j-1] + 1;
      }else{
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
      }
    }
  }
  cout << dp[tmx-1][tmy-1];
}