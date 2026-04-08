class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size= nums.size();
        if(size==0) return 0;
        int k;
        for(int i =0; i<size;i++){
            if(nums[i]>=target){
                k=i;
                break;
            }
        
        }
        return k;
    }
};