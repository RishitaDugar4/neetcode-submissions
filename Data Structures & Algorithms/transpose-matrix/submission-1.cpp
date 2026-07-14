class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        vector<vector<int>> temp;

        for (int i = 0; i < matrix[0].size(); ++i) {
            vector<int> temp1;
            for (int j = 0; j < matrix.size(); ++j) {
                temp1.push_back(matrix[j][i]);
            }
            temp.push_back(temp1);
        }
        return temp;
    }
};