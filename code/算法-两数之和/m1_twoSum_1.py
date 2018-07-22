"""
两数之和：
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
方法：
	暴力搜索
时间复杂度：
	n^2
空间复杂度：
	1
"""


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]


print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
print(Solution().twoSum([1, 2, 3, 4, 5], 8))
print(Solution().twoSum([2, 7, 11, 15], 9))
