class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      max_profit = 0 # profit cant be negative

      left = 0 # buy price

      for right in range(1, len(prices)): #right = sell price
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]

            max_profit = max(max_profit, profit)
        
      return max_profit

    


