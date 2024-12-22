#include <bits/stdc++.h>

using namespace std;


int searchInsert(vector<int>& nums, int target) {
    int right = nums.size()-1;
    int left = 0;
    while(right >= left){
        int mid = left + (right-left)/2;
        if(nums[mid] < target){
            left = mid-1;
        }else if(nums[mid] > target){
            right = mid+1;
        }
        else{
            return mid;
        }
    }return -1;
}

int main(){

}