#LEETCODE 1
## given an array of integers, return indices of te two numbers such that they add up to a specific target

## given nums = [2,7,11,15], target = 9,

## because nums[0] and nums[1] = 2 + 7 = 9,
## return [0,1]

## we will solve using a one pass solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

c = Solution.twoSum([2,7,11,15], 9)
print(c)