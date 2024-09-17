//2019, exploracao do capitao levi

//se existe um tita no (xi, yi) e um outro em (xj, yj)
//ele consegue ir se o coeificiente agular for maior ou igual a p/q
//(yi-yj/xi-xj) >=(p/q)

#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

bool valido(int xi, int yi, int xj, int yj, int p, int q){
  //return (yi-yj)/(xi-xj) >= (p/q);
  long long ys = (long long)(yi- yj) * q; 
  long long xs = (long long)(xi - xj)*p;
  //cout << ys << "-----" << xs << endl;
  return ys >= xs;
}

int main(){
  int n,p,q; //qtd_titas, p, q
  cin >> n >> p >> q;

  vector< tuple<int,int> > coord(n);
  for(int i = 0; i < n; i++){
    int x,y;
    cin >> x >> y;
    coord[i] = make_tuple(x,y);
  }
  int res = 0;
  for(int i = 0; i < n; i++){
    for(int j = i+1; j < n; j++){
      int xi, xj, yi, yj;
      tie(xi, yi) = coord[i];
      tie(xj, yj) = coord[j];
      if(valido(xi, yi, xj, yj, p, q))
        res++;
    }
  }
  cout << endl << res;

}

//30 minutos - NAO RESOLVIDO