class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result(k);
        unordered_map<int, int> counts;

        for (int num : nums) {
            ++counts[num];
        }

        std::priority_queue<pair<int, int>> frequency;
        for (auto& [num, count] : counts) {
            frequency.push({count, num});
        }

        for (int i = 0; i < k; ++i) {
            result[i] = frequency.top().second;
            frequency.pop();
        }

        return result;
    }
};