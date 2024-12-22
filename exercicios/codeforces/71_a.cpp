#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<string> words(n);
    for(int i = 0; i < n; ++i){
        string a; cin >> a;
        words[i] = a;
    }
    vector<string> newWords;
    for(int i = 0; i < n; ++i){
        if(words[i].size() > 10){
            int len = words[i].size()-2;
            string word = words[i][0] + to_string(len) + words[i][words[i].size()-1];
            newWords.push_back(word);
        }else{
            newWords.push_back(words[i]);
        }
    }

    for(int i = 0; i < n; ++i){
        cout << newWords[i] << '\n';
    }
    return 0;
}

// 46 ms