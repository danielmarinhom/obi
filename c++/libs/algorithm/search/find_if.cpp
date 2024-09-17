#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool is_even(int x){
  return x%2 == 0;
}

int main(){
  vector<int> numbers = {1, 3, 5, 7, 8, 10, 12};
  //usando funcao
  auto it = find_if(numbers.begin(), numbers.end(), is_even);
  if(it != numbers.end()){
    cout << "indice: " << it - numbers.begin() + 1 << endl;
  }else{
    cout << "NAO FOI POSSIVEL ACHAR" << endl;
  }
  //usando lambda nelas
  auto it = find_if(numbers.begin(), numbers.end(), [](int x) {
    return x % 2 == 0;
  });
}