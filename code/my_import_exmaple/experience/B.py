print('----------------------------------------------------------')
from variable.experience.A import A

print('A:%d,id:%d' % (A, id(A)))
A = 666
print('A:%d,id:%d' % (A, id(A)))

from variable.experience.A import A

print('A:%d,id:%d' % (A, id(A)))
A = 666 + 1
print('A:%d,id:%d' % (A, id(A)))

print('----------------------------------------------------------')
import variable.experience.A

print('A:%d,id:%d' % (variable.experience.A.A, id(variable.experience.A.A)))
variable.experience.A.A = 777
print('A:%d,id:%d' % (variable.experience.A.A, id(variable.experience.A.A)))

import variable.experience.A

print('A:%d,id:%d' % (variable.experience.A.A, id(variable.experience.A.A)))
variable.experience.A.A = 777 + 2
print('A:%d,id:%d' % (variable.experience.A.A, id(variable.experience.A.A)))

print('----------------------------------------------------------')
import variable.experience.A as AA

print('A:%d,id:%d' % (AA.A, id(AA.A)))
AA.A = 777
print('A:%d,id:%d' % (AA.A, id(AA.A)))

import variable.experience.A as AA

print('A:%d,id:%d' % (AA.A, id(AA.A)))
AA.A = 777 + 2
print('A:%d,id:%d' % (AA.A, id(AA.A)))

# 结论：
# 1.通过from XXX import YYY的方式：
# 可以等效成import XXX.YYY YYY=XXX.YYY，
# 其中的等号含有赋值的作用，所以对YYY的赋值，并不是对XXX.YYY的赋值
# 2.通过import XXX和import XXX as A的方式都是对于根本的操作
