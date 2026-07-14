class Solution {
public:
    bool isPalindrome(string s) {
        std::erase_if(s, [](unsigned char c) {
            return !std::isalnum(c);
        });

        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c) {
            return std::tolower(c);
        });

        int first = 0;
        int last = s.length()-1;

        while (first < last) {
            if (s[first] != s[last]) {
                return false;
            }
            ++first;
            --last;
        }

        return true;
    }
};
