#239. 滑动窗口最大值
#给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#返回 滑动窗口中的最大值 
#思路（个人看了题解之后的想法）：用一优化队列的，队列由滑动窗口中每个元素删去左侧所有比自身小的元素，则得等得到的优化队列是一个从左往右递减的列表。实际上每个窗口中最大的值即为优化队列最左侧的元素。每次窗口滑动，考虑队首是否还在队列中，并考虑最新加入队尾的元素。
#先搬题解，要补一下算法知识
#算法流程：
#1. 初始化： 双端队列  ，结果列表  ，数组长度  ；
#2. 滑动窗口： 左边界范围  ，右边界范围  ；
#a. 若  且 队首元素  被删除元素  ：则队首元素出队；
#b. 删除  内所有  的元素，以保持  递减；
#c. 将  添加至  尾部；
#d. 若已形成窗口（即  ）：将窗口最大值（即队首元素  ）添加至列表  ；
#3. 返回值： 返回结果列表  ；
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res


