//um terreno pode ser dividido apenas usando uma sequencia de divisoes de terreno
//uma divisao de terreno eh uma opeacao que divide um terreno em duas partes
//para cada divisao de terreno deve ser pago um imposto

//Parte maior * fator
//para dividir n lotes, sao necessarias n-1 divisoes e n-1 pagamentos

#include <bits/stdc++.h>

using namespace std;

int maior(vector<int> &u){
  int maior = u[0];
  for(int i = 1; i < u.size(); ++i){
    if(u[i] > maior){
      maior = u[i];
    }
  }
  cout << maior << '\n';
  return maior;
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  float f;
  cin >> n >> f;
  vector<int> areas(n);
  for(int i = 0; i < n; ++i){
    cin >> areas[i];
  }
  float valor = (maior(areas) * f) * (n-1)*(n-1*f);
  cout << valor;
}
//nao concluido - dp