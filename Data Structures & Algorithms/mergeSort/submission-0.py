# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)


    def mergeSortHelper(self, pairs: List[Pair], start: int, end:int) -> List[Pair]:
        if end-start+1 <= 1:
            return pairs

        mid = (start+end)//2

        self.mergeSortHelper(pairs, start, mid)
        self.mergeSortHelper(pairs, mid+1, end)

        self.merge(pairs, start, mid, end)

        return pairs

    def merge(self, pairs: List[Pair], start:int, mid: int, end:int) -> None:
        left_arr = pairs[start: mid+1]
        right_arr = pairs[mid+1: end+1]

        i = 0
        j = 0
        k = start

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].key <= right_arr[j].key:
                pairs[k] = left_arr[i]
                i+=1
            else:
                pairs[k] = right_arr[j]
                j+=1

            k+=1

        while i < len(left_arr):
            pairs[k] = left_arr[i]
            i+=1
            k+=1

        while j < len(right_arr):
            pairs[k] = right_arr[j]
            j+=1
            k+=1



