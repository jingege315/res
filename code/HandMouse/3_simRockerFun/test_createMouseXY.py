import createMouseXY
from unittest import TestCase


# 此文件是在电脑上仿真的，增加仿真的方面，和完整性
class TestGetValue(TestCase):
	def test_all(self):
		for i in range(-200, 200):
			value = i / 100
			if -100 <= i <= 100:
				# 正常
				ret_x, ret_y = createMouseXY.getValue(value, value)
				self.assertEqual(ret_x, value * createMouseXY.factor_mul_x)
				self.assertEqual(ret_y, value * createMouseXY.factor_mul_y)
			else:
				# 不正常的值
				try:
					ret_x, ret_y = createMouseXY.getValue(value, value)
				except:
					pass
				else:
					self.fail('没有异常，不对')
