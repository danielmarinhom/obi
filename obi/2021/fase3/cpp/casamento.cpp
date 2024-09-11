//A e B terem o mesmo numero de digitos
//o digito de menor valor da posicao i eh eliminado, se = nenhum eh eliminado

#include <bits/stdc++.h>

using namespace std;

int main(){
  string n1, n2;
  cin >> n1 >> n2;
  while (n1.size() > n2.size()) n2 = '0' + n2;
  while (n1.size() < n2.size()) n1 = '0' + n1;

  string casado1, casado2;
  for(int i = 0; i < n1.size(); i++){
    if(n1[i] == n2[i]){
      casado1 += n1[i];
      casado2 += n2[i];
    }
    else if(n1[i] > n2[i]) casado1 += n1[i];
    else casado2 += n2[i];
  }
  int res1, res2;
  if(casado1.size() == 0) res1 = -1;
  else res1 = stoi(casado1);
  if(casado2.size() == 0) res2 = -1;
  else res2 = stoi(casado2);
  cout << min(res1, res2) << " " << max(res1, res2);
}