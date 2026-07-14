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
    void quickSortHelper(vector<Pair>& pairs, int start, int end) {
        if (end - start + 1 <= 1) {
            return;
        }

        Pair pivot = pairs[end];
        int left = start;

        for (int i = start; i < end; ++i) {
            if (pairs[i].key < pivot.key) {
                Pair temp = pairs[left];
                pairs[left] = pairs[i];
                pairs[i] = temp;
                
                left += 1;
            }
        }

        pairs[end] = pairs[left];
        pairs[left] = pivot;

        quickSortHelper(pairs, start, left-1);
        quickSortHelper(pairs, left+1, end);

    }
    
    vector<Pair> quickSort(vector<Pair>& pairs) {
        quickSortHelper(pairs, 0, pairs.size()-1);
        return pairs;
    }
};
