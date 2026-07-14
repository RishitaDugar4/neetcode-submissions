class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf = 0;
        int minBuy = prices[0];

        for (int& price : prices) {
            maxProf = max(maxProf, price - minBuy);
            minBuy = min(minBuy, price);
        }

        return maxProf;
    }
};
