"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input example: [1,2,3,4]
        output example: [24,12,8,6]
        """
        newList = [x for x in nums if x != 0]
        result = numpy.prod(newList)
        output = []
        for i in nums:
            if i != 0:
                output.append(int(result / i))
            else:
                output.append(0)

        return(output)