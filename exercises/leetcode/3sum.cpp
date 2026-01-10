#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> res;
    set<vector<int>> triplets;
    sort(nums.begin(), nums.end());
    for(int i = 0; i < nums.size(); ++i){
        int j, k;
        j = i+1; k = nums.size()-1;
        while(k > j){
            int sum = nums[i]+nums[j]+nums[k];
            if(sum == 0){
                triplets.insert({nums[i], nums[j], nums[k]});
            }
            k--;j++;
        }
        
    }      
    for(const auto x : triplets){
        res.push_back(x);
    }
    return res; 
}

int main(){
    
}