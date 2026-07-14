// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> mergeSort(vector<Pair>& pairs) {
        mergeSortHelper(pairs, 0, pairs.size()-1);
        return pairs;
    }

    void mergeSortHelper(vector<Pair>& pairs, int start, int end) {
        if (end - start + 1 <= 1) {
            return;
        }

        int mid = (start + end) / 2;

        mergeSortHelper(pairs, start, mid);
        mergeSortHelper(pairs, mid+1, end);

        merge(pairs, start, mid, end);
    }

    void merge(vector<Pair>& pairs, int start, int mid, int end) {
        vector<Pair> left(pairs.begin() + start, pairs.begin() + mid + 1);
        vector<Pair> right(pairs.begin() + mid + 1, pairs.begin() + end + 1);

        int i = 0;
        int j = 0;
        int k = start;

        while (i < left.size() && j < right.size()) {
            if (left[i].key <= right[j].key) {
                pairs[k] = left[i];
                ++i;
            } else {
                pairs[k] = right[j];
                ++j;
            }
            ++k;
        }

        while (i < left.size()) {
            pairs[k] = left[i];
            ++i;
            ++k;
        }

        while (j < right.size()) {
            pairs[k] = right[j];
            ++j;
            ++k;
        }
    }
};
