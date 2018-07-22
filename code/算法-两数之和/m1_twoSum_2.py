"""
两数之和：
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
方法：
	使用排序之后，对数组进行搜索的办法
时间复杂度：
	marge排序：n * log n
	搜索：n
	总计：n * log n
空间复杂度：
	marge排序：n
	搜索：1
	总计：n
"""

from math import floor
from copy import copy as py_copy


def argsort(nums):
	arg = list(range(len(nums)))

	def get(i, list_index=None):
		if list_index is None:
			list_index = arg
		return nums[list_index[i]]

	def set(i, index):
		arg[i] = index

	def copy(start, end):
		return py_copy(arg[start:end + 1])

	def sort_merge_core(start, end):
		"""
		merge排序
		分治策略：
		分解：数组二分，每个小数组排序
		解决：对于最小的数组，长度1，不需要排序
		合并：两个有序的数组，合并成为一个有序的数组
		start：排序的头指针，包括本身
		mid：分解的中间指针，i~j是分解的第一个数组，j+1~k是分解的第二个数组
		end：排序的尾指针，包括本身
		"""
		if start < end:
			mid = floor((start + end) / 2)
			sort_merge_core(start, mid)
			sort_merge_core(mid + 1, end)
			merge(start, mid, end)

	def merge(start, mid, end):
		"""
		合并
		i1：第一个数组的指针，还没有发到的位置
		i2：第二个
		index：发牌的指针，指向A，说明将要需要放置的位置
		"""
		i1, i2 = 0, 0
		A1 = copy(start, mid)
		A2 = copy(mid + 1, end)

		for index in range(start, end + 1):
			if i2 == len(A2) or i1 != len(A1) and get(i1, A1) < get(i2, A2):
				set(index, A1[i1])
				i1 += 1
			else:
				set(index, A2[i2])
				i2 += 1

	sort_merge_core(0, len(nums) - 1)
	return arg


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		start = 0
		end = len(nums) - 1

		# 从小到大排序，并保存原来的顺序
		nums_index = argsort(nums)
		print()
		print(nums,target)
		print(nums_index)

		def getSum():
			return nums[nums_index[end]] + nums[nums_index[start]]

		# start和end之和刚刚大于等于target
		while getSum() > target:
			end -= 1
		if getSum() < target and end + 1 < len(nums):
			end += 1

		# 开始寻找，如果小于start增加，如果大于end减少
		while True:
			if start >= end:
				return None
			if getSum() < target:
				start += 1
			elif getSum() > target:
				end -= 1
			else:
				return sorted([nums_index[start], nums_index[end]])


print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
print(Solution().twoSum([1, 2, 3, 4, 5], 8))
print(Solution().twoSum([2, 7, 11, 15], 9))
