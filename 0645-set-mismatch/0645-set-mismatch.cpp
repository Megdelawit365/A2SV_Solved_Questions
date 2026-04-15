class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int num = -1;
        vector<int> result;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]==num){
                result.push_back(num);
                result.push_back(num+1);
            }else{
                num = nums[i];
            }
        }
        return result;
    }
};