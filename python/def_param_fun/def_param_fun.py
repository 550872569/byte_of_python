'''
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回

定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
'''

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        return None
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs(-99))
# 99

# no result \ return function
def printInput(x):
    print(x)

# print(printInput('10'))
# 10
# None

# print(my_abs('A'))
# None

def replaceNumber(a, b):
    return b, a

# print(replaceNumber(12, 99))
# (99, 12)


# ax2+bx+c=
def sum(a, b, c):
    if not isinstance(a, (int, float)):
        return None
    if not isinstance(b, (int, float)):
        return None
    if not isinstance(c, (int, float)):
        return None
    return a+b+c

# print(sum(12, 23, 34))
# 69

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# print(power(5, 2))
# 25

def powerDefault(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# print(powerDefault(5))
# 25

'''
设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，
否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

 定义默认参数要牢记一点：默认参数必须指向不变对象！

'''

def add_end(L=[]):
    s = []
    L.append('END')
    return L

# print(add_end())
# print(add_end())
# ['END']
# ['END', 'END']

# def addToEnd(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# print(addToEnd())
# print(addToEnd())

# ['END']
# ['END']



# 要定义出这个函数，我们必须确定输入的参数。
# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，
# 这样，函数可以定义如下
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3, 5]))
'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''