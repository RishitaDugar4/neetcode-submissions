class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        int index = 1;
        for (int i = 1; i < size(nums); ++i) {
            if (nums[i] != nums[i-1]) {
                nums[index] = nums[i];
                index ++;
            }
        }

        return index;
        
    }
};