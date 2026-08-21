class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        median is center most value in a sorted list

        need to combine list1 and list2 => list3
        need to find center, more importantly
        '''

        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        print(nums3)

        mid = len(nums3) // 2
        if len(nums3) % 2 == 1:
            return nums3[mid]
        else:
            left = mid - 1
            right = mid
            print(left, right, nums3[left], nums3[right])
            return float(nums3[left] + nums3[right]) / 2

