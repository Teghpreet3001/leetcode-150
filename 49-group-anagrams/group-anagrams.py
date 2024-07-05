class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for word in strs:
            wordKey = tuple(sorted(word)) #use tuple for keys
            if wordKey in map:
                map[wordKey].append(word)
            else: 
                map[wordKey] = [word] 
        return list(map.values())

    