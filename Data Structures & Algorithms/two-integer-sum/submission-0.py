class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}
        for i, num in enumerate(nums):
            n = target - num

            if n in total:
                return [total[n], i]
            
            total[num] = i
        
        return total

     
   
        
