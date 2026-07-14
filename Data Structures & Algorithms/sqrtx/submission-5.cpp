class Solution {
public:
    int mySqrt(int x) {
        int low = 0;
        int high = x;
        int result = -1;

        if (x <= 1) { return x; }

        while (low <= high) {
            int mid = std::floor((low + high) / 2);
            if (mid > x / mid) {
                high = mid - 1;
            } 
            else if (mid <= x / mid) {
                low = mid + 1;
                result = mid;
            }
            else {
                return result;
            }
        }
        return result;
    }
};