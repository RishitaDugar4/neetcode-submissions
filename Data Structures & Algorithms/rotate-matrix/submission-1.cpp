class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();
        vector<vector<int>> rotated(size, vector<int>(size));

        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                rotated[j][size - 1 - i] = matrix[i][j];
            }
        }

        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                matrix[i][j] = rotated[i][j];
            }
        }
    }
};
