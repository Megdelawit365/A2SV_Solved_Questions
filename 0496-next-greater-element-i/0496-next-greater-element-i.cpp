class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_map<int,int> map;
        stack<int> stack;
        for(int i=0; i<nums2.size();i++){
            while(!stack.empty() && nums2[i]>stack.top()){
                map[stack.top()]=nums2[i];
                    stack.pop();
            }
            
            stack.push(nums2[i]);
        }

        
            for(int i:nums1){
                if(map.count(i)){
                    result.push_back(map[i]);
                }else{
                    result.push_back(-1);
                }
            }
            return result;


    }
};