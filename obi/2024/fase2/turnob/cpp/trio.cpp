#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> palitos(n);
  for(int i = 0; i < n; i++){
    cin >> palitos[i];
  }
  sort(palitos.begin(), palitos.end());
  int soma = 0;
  for(int i = 0; i < n-2; i++){
    for(int j = i+1; j < n-1; j++){
      int k = j + 1;
      while(k < n and palitos[i] + palitos[j] > palitos[k]){
        k++;
      }
        soma += (k-j-1);
    }
  }
  cout << soma;
}