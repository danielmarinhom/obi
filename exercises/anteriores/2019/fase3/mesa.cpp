#include <iostream>
#include <map>

using namespace std;

int main(){
  //ana sorteia um inteiro A e comecando da cadeira 1 em anti horario, conta A cadeiras e senta
  //beatriz sorteia um inteiro B e faz o mesmo, se ana estiver nela, senta um pra frente
  //carolina senta na que estiver livre
  int ana, bea;
  cin >> ana >> bea;
  map<int, bool> lugares = {{1, false},{2, false},{0, false}};
  auto it = lugares.begin();
  for(int i = 0; i < ana; i++){
    if (it[0] < lugares.size()){
      ++it;
    }
  }
}