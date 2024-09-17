#include <bits/stdc++.h>
#include <numeric>

using namespace std;

void alterar(vector<int>& s, int i, int v){
  s[i-1] = v;
}
int lmc(vector<int> s){
  int mdc = s[0];
  for(int i = 1; i <= s.size(); i++){
    mdc = gcd(mdc, s[i]);
    if(mdc == 1)
      break;
  }
}

int main(){
  //candidato if lmc > 1
  //alterar o valor de um elemento da sequencia
  //consultar o numero de subsequencias candidatas em um dado trecho
  int n,m;
  cin >> n >> m; //elementos, operacoes
  vector<int> s(n);
  for(int i = 0; i < n; i++)
    cin >> s[i];
  
  for(int i = 0; i < m; i++){

  }

}