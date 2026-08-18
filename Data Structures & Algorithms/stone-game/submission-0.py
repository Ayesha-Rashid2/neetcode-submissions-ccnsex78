class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        turn = 1

        while piles:
            if piles[0] >= piles[-1]:
                total = piles[0]
                piles.pop(0)
            else:
                total = piles[-1]
                piles.pop()
            
            if turn % 2 == 1:
                alice += total
            else:
                bob += total

        return True if alice > bob else False
        