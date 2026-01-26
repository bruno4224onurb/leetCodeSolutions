class Solution:
    @staticmethod
    def merge(a, b):
        result = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i +=1
            else:
                result.append(b[j])
                j +=1
        result.extend(a[i:])
        result.extend(b[j:])
        return result

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        F = self.merge(nums1, nums2)
        if len(F) % 2 == 0:
            median = (F[(len(F) - 1)//2] + F[len(F)//2])/2.0
        else:
            median = F[len(F)//2]

        return median 

        
