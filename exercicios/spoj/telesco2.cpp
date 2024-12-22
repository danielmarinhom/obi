#include <iostream>

using namespace std;

int main(){
  //100 mm2 de area
  //40.000.000 fotons/s - telescopio
  //400.000 fotons/s - pupila
  int a, n, resultado;
  cin >> a >> n;
  
  const int fotons_necessarios = 40000000;

  int res = 0;
  for(int i = 0; i < n; i++){
    int f;
    cin >> f;
    if(a*f >= fotons_necessarios)
      res++;
  }

  cout << res;

}