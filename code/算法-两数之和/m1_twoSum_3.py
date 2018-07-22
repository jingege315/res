"""
两数之和：
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
方法：
	使用hash建立 item->index 的映射关系，通过 target-item 反向寻找是否存在这个index
时间复杂度：
	hash映射：n
	反向寻找：n
	总计：n
空间复杂度：
	hash映射：n
	反向寻找：1
	总计：n
"""


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		hash_ = dict(zip(nums, range(len(nums))))
		for i in range(len(nums)):
			other=target-nums[i]
			if hash_.get(other):
				return [i,hash_[other]]

print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
print(Solution().twoSum([1, 2, 3, 4, 5], 8))
print(Solution().twoSum([2, 7, 11, 15], 9))
