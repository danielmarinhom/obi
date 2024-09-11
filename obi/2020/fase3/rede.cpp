//indice de repostaram = usuarios que repostaram
//fator de influencia = maximo valor de FI tal que U postou FI mensagens que, cada uma, tem um índice de repostagem de pelo menos FI.
//4 mensagens com IR 1,1,5,6 seu FI = 2 pois 2 mensagens com indice de repostagem maior ou igual a 2

#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> ir(n);

  for(int i = 0; i < n; i++){
    cin >> ir[i];
  }
  sort(ir.begin(), ir.end());
  int fi = 0;
  for(int i = 0; i < n; i++){
    if(ir[i] >= n-1){
      fi = n-1;
    }
  }
  cout << "reposta: " << fi << endl;
  return 0; 
}