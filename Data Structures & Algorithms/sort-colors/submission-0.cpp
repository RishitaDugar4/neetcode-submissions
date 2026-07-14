class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> counts(3);

        for (int& num : nums) {
            counts[num] += 1;
        }

        int index = 0;
        for (int i = 0; i < counts.size(); ++i) {
            while (counts[i]-- > 0) {
                nums[index++] = i;
            }
        }
        
    }
};