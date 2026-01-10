//2021 - Falha de seguranca

#include <bits/stdc++.h>

using namespace std;

bool verificarSenha(string a, string b){
  return a.find(b) != string::npos;
}

int main(){
  //tem que ter a string inteira dentro da outra
  //quantos pares de A,B o A usando sua senha consegue acesso ao B
  int n;
  cin >> n;
  string senhas[n];
  //vector< tuple<string, string> > usados;
  for(int i = 0; i < n; i++){
    cin >> senhas[i];
  }
  int res = 0;
  for(int i = 0; i < n; i++){
    for(int j = i+1; j < n; j++){
      if(verificarSenha(senhas[i], senhas[j])){
        res++;
        cout << senhas[i] << " " << senhas[j] << endl;
      }
    }
  }
  cout << res;

}
//FINALIZADO MAS ERRADO