#1. 两数之和
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

#你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

#你可以按任意顺序返回答案。

#法一：暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []#若无解要记得返回空列表

#法二：哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):#enumerate将列表中每一个元素返回成一个元组，由索引和原来的值构成
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i   #此处将列表中元素作为键
        return []

