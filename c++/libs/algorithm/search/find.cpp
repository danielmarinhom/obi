#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  vector<int> numbers = {6, 5, 4, 1, 9, 66, 12, 63, 97};
  int target;
  cin >> target;
  auto it = find(numbers.begin(), numbers.end(), target);
  if(it != numbers.end()){
    cout << "Indice: " << it - numbers.begin() + 1 << endl;
  }else{
    cout << "INDICE NAO ENCONTRADO" << endl;
  }
}