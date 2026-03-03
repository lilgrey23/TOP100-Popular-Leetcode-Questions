#438. 找到字符串中所有字母异位词
#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#个人错解：
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ind=[]
        p_=sorted(p)
        for i in range(len(s)-len(p)+1):
            if s[i] not in p:
                continue
            if s[i:len(p)].sort()==p_:#这里不能用sort()
                ind.append(i)
        return ind
    
    #官方解答
    class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):#左侧从s[0]开始
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):#窗口不断滑动，减去最左边一项，加上最右边一项
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            
            if s_count == p_count:
                ans.append(i + 1)

        return ans
#记住asc码相对值
