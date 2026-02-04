#49. 字母异位词分组
#给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#示例 1:

#输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

#输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

#解释：

#在 strs 中没有字符串可以通过重新排列来形成 "bat"。
#字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
#字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

#法一
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            s_ = "".join(sorted(s))#排序
            if s_ not in table:
                table[s_] = [s]
            else:
                table[s_].append(s)
        return list(table.values())

#法二
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)  # 如果 key 不在字典中，则自动插入一个空列表。如果是普通字典则会报错。
        for s in strs:
            sorted_s = ''.join(sorted(s))  # 把 s 排序，作为哈希表的 key
            d[sorted_s].append(s)  # 排序后相同的字符串分到同一组
        return list(d.values())  # 哈希表的 value 保存分组后的结果