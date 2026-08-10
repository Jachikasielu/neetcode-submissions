class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            target = tuple(sorted(i))
            if target not in anag:
                anag[target] = []
            anag[target].append(i)
        return list(anag.values())
