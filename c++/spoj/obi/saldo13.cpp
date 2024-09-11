#include <iostream>

using namespace std;

int main(){
  int n,s;
  cin >> n >> s;
  int lowest = s;
  for(int i = 0; i < n; i++){
    int x;
    cin >> x;
    s += x;
    if(s <= lowest)
      lowest = s;
  }
  cout << lowest;
}