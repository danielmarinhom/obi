#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void sortRegular(vector<int> actual){
  sort(actual.begin(), actual.end());
  for(int valor : actual){
    cout << valor << " ";
  }
}
void sortPartial(vector<int> actual){
  partial_sort(actual.begin(), actual.begin() + 3, actual.end());
  for(int valor : actual){
    cout << valor << " ";
  }
}

int main(){
  vector<int> numbers = {4, 6, 1, 9, 11, 5};
  cout << "SEM SORT:" << endl;
  for(int valor : numbers){
    cout << valor << " ";
  }
  cout << endl;
  cout << "REGULAR SORT:" << endl;
  sortRegular(numbers);
  cout << endl << "PARTIAL SORT +3:" << endl;
  sortPartial(numbers);
  return 0;
}