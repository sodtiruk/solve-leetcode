from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums == None:
            return [-1, -1]
        
        hashMap = {}
        i = 0
        while i < len(nums):
            if hashMap.get(nums[i]) != None:
                index = hashMap.get(nums[i])
                return [index, i]
            else:
                res = target - nums[i]
                hashMap[res] = i
            i += 1 






        


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))


