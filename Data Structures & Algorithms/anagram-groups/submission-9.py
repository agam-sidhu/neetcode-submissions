class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            val = ''.join(sorted(s))
            if val in dic:
                dic[val].append(s)
            else:
                dic[val] = [s]
        return list(dic.values())