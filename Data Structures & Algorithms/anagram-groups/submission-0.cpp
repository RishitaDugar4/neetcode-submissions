class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> words;

        for (int i = 0; i < strs.size(); ++i) {
            string s = strs[i];
            sort(s.begin(), s.end());
            words[s].push_back(strs[i]);
        }

        vector<vector<string>> result;
        for (auto& word : words) {
            result.push_back(word.second);
        }

        return result;
    }
};
