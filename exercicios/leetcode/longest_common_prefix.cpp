#include <bits/stdc++.h>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    string longest = strs[0];
    //flower flow flight
    if(strs.empty()) return "";
    for(int i = 1; i < strs.size(); ++i){
        while(strs[i].find(longest) != 0){
            longest = longest.substr(0, longest.size()-1);
            if(longest.empty()) return "";
        }
    }
    return longest;
}


int main(){

}