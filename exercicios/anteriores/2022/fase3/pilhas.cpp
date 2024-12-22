//2022 Pilha de Moedas

#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main(){
  int n, k;
  cin >> n >> k;
  vector<int> pilhas(n);
  for(int i = 0; i < n; i++){
    cin >> pilhas[i];
  }
  sort(pilhas.begin(), pilhas.end());
  int moedas = 0;
  for(int i = 1; i < n; i++){
    if(pilhas[i] > pilhas[i-1]){
      moedas++;
    }
  }
  cout << moedas;
}