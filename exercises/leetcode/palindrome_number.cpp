#include <bits/stdc++.h>

using namespace std;

bool isPalindrome(int x) {
    if(x < 0 || (x != 0  &&  x % 10 == 0)){return false;}
    if(x <= 9){return true;}

    string comp = to_string(x);
    int right = comp.size()-1; int left = 0;

    while(right > left){
        if(comp[right] != comp[left]){return false;}
        left++; right--;
    }
    return true;
}

int main(){
    cout << isPalindrome(121);
}