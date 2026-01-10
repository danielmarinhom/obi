#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    string x;
    cin >> x;
    int valor = stoi(x[0]);
    for(int i = 2; i < n; i+=2){
        char op = x[i-1];
        if(op == '-'){
            valor -= stoi(x[i]);
        }else{
            valor += stoi(x[i]);
        }
    }
    cout << valor;
}