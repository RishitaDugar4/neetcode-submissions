class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());
        int result = high;

        while (low <= high) {
            int mid = (low + high) / 2;
            int hours = 0;

            for (int pile : piles) {
                hours += ceil(static_cast<double>(pile) / mid);
            }

            if (hours > h) {
                low = mid + 1;
            } else {
                result = mid;
                high = mid - 1;
            }
        }
        return result;
    }
};
