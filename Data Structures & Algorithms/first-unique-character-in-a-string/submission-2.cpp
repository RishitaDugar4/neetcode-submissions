class Solution {
public:
    int firstUniqChar(string s) {
        std::map<char, int> counts;

        for (int i = 0; i < s.length(); ++i) {
            if (counts.contains(s[i])) {
                ++counts[s[i]];
            }
            else {
                counts[s[i]] = 1;
            }
        }

        for (int i = 0; i < s.length(); ++i) {
            if (counts[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};