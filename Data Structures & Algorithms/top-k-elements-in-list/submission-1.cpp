class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        std::vector<int> result(k);

        for (int& num : nums) {
            ++counts[num];
        }

        std::priority_queue<pair<int, int>> frequencies;
        for (auto& [num, i] : counts) {
            frequencies.push({i, num});
        }

        for (int i = 0; i < k; ++i) {
            result[i] = frequencies.top().second;
            frequencies.pop();
        }

        return result;
    }
};
