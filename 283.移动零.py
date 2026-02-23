#283.移动零
#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#个人第一次做对的解法
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]!=0:
                continue
            for j in range(i+1,len(nums)):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
        return nums#方法耗时长
    #官方解答
    class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1#只要右指针对应非零数，即移到左边
