# 此文件输入X，Y的百分比，生成鼠标移动的X，Y值

factor_mul_x = 10
factor_mul_y = 10


# 命令中，您将发送4条信息：按钮状态，x，y和滚动。
# 数字10告诉PC机鼠标在x方向移动10个像素
def getValue(value_x, value_y):
	assert -1 <= value_y <= 1 and -1 <= value_x <= 1
	return value_x * factor_mul_x, value_y * factor_mul_y
