class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for st in strs:
            key = tuple(sorted(st))
            if key in dictionary:
                dictionary[key].append(st)
            else:
                dictionary[key] = [st]
        return list(dictionary.values())
