#3. 无重复字符的最长子串
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

#思考：每次从第k个字母开始，找不包含重复字符的最长子串，rk表示这个子串最后一个字母的位置。不难发现rk关于k为递增。则容易想到双指针。从左枚举开头的字母，向右不断找不重复的字母
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
