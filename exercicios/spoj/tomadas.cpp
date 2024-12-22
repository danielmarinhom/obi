#include <iostream>

using namespace std;

int main(){
  int t1, t2, t3, t4;
  cin >> t1 >> t2 >> t3 >> t4;
  int res = 0;
  res += (t1-1) + (t2-1) + (t3-1) + (t4);
  cout << res;
}
