class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        
        if len(s) != len(t):
            return False
                
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        for j in t:
            if j in map:
                map[j] -= 1
            else:
                map[j] = 0
        
        count = map.values()

        for k in count:
            if k != 0:
                return False
        return True