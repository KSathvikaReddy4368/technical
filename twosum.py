class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        l=0
        for i in range(len(nums)+1):
            for j in range(i,n):
                if nums[i]+nums[j]==target:
                    if i==j:
                        l=l
                    else:
                        l=[i,j]
        return l
