#include <iostream>

using namespace std;

bool canDivide(int n){
    return n % 2 == 0 && n >= 4;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    bool res = canDivide(n);
    if(res){
        cout << "YES";
    }else{
        cout << "NO";
    }
    return 0;

}

// 124ms