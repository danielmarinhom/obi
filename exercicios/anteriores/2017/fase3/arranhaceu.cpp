//2017 - Arranha-ceu

#include <bits/stdc++.h>

using namespace std;

void mudanca(vector<int> &a, int &p, int &k){
  a[k] = p;
}
int bombeiro(vector<int> &a, int &k){
  int pessoas = 0;
  for(int i = 0; i < k; ++i){
    pessoas += a[i];
  }
  return pessoas;
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  //mudanca - altera o numero de pessoas que mora num andar
  //bombeiro - informa o total de pessoas que moram do 1 ate k inclusive
  int n, q; //numero de andares e eventos
  cin >> n >> q;
  vector<int> andares(n, 0), respostas;
  for(int i = 0; i < n; ++i){
    int a;
    cin >> a;
    andares[i] = a;
  }
  for(int i = 0; i < q; ++i){
    int op, k;
    cin >> op >> k;
    if(op == 0){
      int p;
      cin >> p;
      k--;
      mudanca(andares, p, k);
    }
    else if(op == 1){
      int res = bombeiro(andares, k);
      respostas.push_back(res);
    }
  }

  for(int i = 0; i < respostas.size(); ++i){
    cout << respostas[i] << '\n';
  }

}
//PERFEITO - 15 min