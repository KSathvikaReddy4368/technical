class Solution:
    # Brute Force approach: O(n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Set variables:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        output = []
        
        # 1) Merge the sorted arrays:
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j += 1
                
        output = output + nums1[i:] + nums2[j:]
            
        # 2) Find the median:
        n = len(output)
        median = 0
        
        # Merged array has even length:
        if n % 2 == 0:
            idx1 = (n//2)-1
            idx2 = idx1+1
            median = (output[idx1]+output[idx2])/2
            
        # Merged array has odd length:
        else:
            idx = n//2
            median = output[idx]
            
        return median
        
