# Runtime: 20 ms
# Memory Usage: 14 MB
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones[0]
        while len(stones) > 2:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            stones.append(abs(x-y))
            
        if len(stones) == 2:
            
            if (stones[0]!=stones[1]):
                return abs(stones[0] - stones[1])
            
            else:
                return 0
        
        return res
