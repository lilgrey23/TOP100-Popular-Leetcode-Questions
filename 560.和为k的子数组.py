#560. 和为 K 的子数组
#给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。子数组是数组中元素的连续非空序列。
#key 前缀和，即前面n个数字的和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)#加一防止遗漏单个的情况
        for i, x in enumerate(nums):#s储存前缀和
            s[i + 1] = s[i] + x

        cnt = defaultdict(int)#cnt是是一个哈希表，储存前缀和的出现次数
        ans = 0
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans


