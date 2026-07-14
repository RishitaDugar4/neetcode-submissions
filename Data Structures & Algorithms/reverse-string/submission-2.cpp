class Solution {
public:
    void reverseString(vector<char>& s) {
        char first = 0;
        char last = s.size()-1;

        while (first < last) {
            char temp = s[first];
            s[first] = s[last];
            s[last] = temp;

            ++first;
            --last;
        }
    }
};