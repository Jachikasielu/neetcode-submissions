class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L <= R:
            c = numbers[L] + numbers[R]
            if c == target:
                return [L + 1, R + 1]
            elif c < target:
                L += 1
            else:
                R -= 1
        return []



