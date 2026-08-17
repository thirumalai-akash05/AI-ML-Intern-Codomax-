class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1={}
        for index,value in enumerate(nums):
            diff=target-value
            if diff in nums1:
                return[nums1[diff],index]
            nums1[value]=index

        
