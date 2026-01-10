#include <bits/stdc++.h>

using namespace std;

bool isMatch(string s, string p) {
    if(s.size() != p.size()){
        int contagem = 0;
        for(int i = 0; i < p.size(); ++i){
            if(p[i] != '*'){contagem++;}
        }
        if(contagem != p.size() || contagem != s.size()){return false;}
    }
    for(int i = 0; i < s.size(); ++i){
        if((s[i] != p[i] && p[i] != '.')
            &&
            (s[i] != p[i] && (p[i] == '*' && s[i] != p[i-1]))
            && (s[i] == '.' && s[i-1] != '*'))
        {
            return false;
        }
    }
    return true;
}

int main(){
}
// errado