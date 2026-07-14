class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majInt = -1;
        int result = -1;
        map<int, int> majority;

        for (int i = 0; i < nums.size(); ++i) {
            if (majority.contains(nums[i])) {
                ++majority[nums[i]];
            } else {
                majority[nums[i]] = 1;
            }
        }

        for (auto const& [key, val] : majority) {
            if (val > majInt) {
                majInt = val;
                result = key;
            }
        }
        return result;
    }
};