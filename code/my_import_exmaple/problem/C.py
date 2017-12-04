from A import num
from B import get_num


def set_num(num_in):
	global num
	num = num_in
	print("set_num:", num)


if __name__ == '__main__':
	set_num(100)
	print("main:", get_num())
