class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> sums;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];

            if (sums.find(complement) != sums.end()) {
                return {sums[complement], i};
            }

            sums.insert({nums[i], i});
        }
        return {};
    }
};
