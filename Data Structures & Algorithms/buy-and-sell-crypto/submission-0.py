class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       min_p = float("inf")
       total = 0
       for p in prices:
        min_p = min(p, min_p)
        total = max(total, p - min_p)

       return total


       
    
        

