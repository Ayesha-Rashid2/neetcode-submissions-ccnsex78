class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_used = 0
        floors = 0
        
        while coins_used + (floors + 1) <= n:
            floors += 1
            coins_used += floors
        return floors