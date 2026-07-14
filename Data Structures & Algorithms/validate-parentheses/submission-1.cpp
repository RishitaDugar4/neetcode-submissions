class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stacked;
        std::map<char, char> pairs = { 
            { '}', '{'},
            { ']','[' }, 
            { ')','(' } 
        };

        for (char c : s) {
            if (pairs.count(c)) {
                if (!stacked.empty() && stacked.top() == pairs[c]) {
                    stacked.pop();
                } else {
                    return false;
                }
            } else {
                stacked.push(c);
            }
        }
        return size(stacked) == 0;
    }
};
