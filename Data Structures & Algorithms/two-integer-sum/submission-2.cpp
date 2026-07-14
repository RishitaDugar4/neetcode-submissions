class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numSum;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (numSum.find(complement) != numSum.end()) {
                return {numSum[complement], i};
            }
            numSum.insert({nums[i], i});
        }
        return {};
    }
};
