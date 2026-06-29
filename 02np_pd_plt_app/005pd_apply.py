# 3.8adas的apply函数
# apply()函数可以对DataFrame或Series的数据进行逐行、逐列或逐元素的操作。可以使用自定义函数对数据进行变换、计算或处理，通常用于处理复杂的变换逻辑，或者处理不能通过向量化操作轻松完成的任务。
# 3.8.1Series使用apply()
import pandas as pd
# Series的apply方法调用的函数，参数接收的是Series中的一个元素
def func(item):
  return item * 20

s = pd.Series([10, 20, 30])
print(s.apply(func))
# 也可以传入lambda表达式。
print(s.apply(lambda item: item * 20))
# 传入带参数的函数。
# apply()方法会将自己没有匹配上的参数，在调用func的时候作为func的参数传递过去,必须通过关键字传参
def func1(item,p1):
  return item * p1
print(s.apply(func1,p1=3))
# 3.8.2DataFrame使用apply()
# DataFrame的apply方法调用的函数，参数接收的是DataFrame中的一个Series
def func(s):
  return s.sum()

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
print(df.apply(func))

#默认axis=0，按行方向进行操作，对列进行统计；
#可以设置axis=1，按照列的方向进行操作，对行进行统计
print(df.apply(func, axis=1))


def func(s):
  return s["a"] / s["b"]

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
print(df.apply(func, axis=1))
# 0  0.25
# 1  0.40
# 2  0.50
# dtype: float64

import numpy as np
# def f(x, y):
#   if y == 0:
#     return np.nan
#   return x / y

# df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
# print(f(df["a"], df["b"])) # ValueError
# 上述代码会报错，因为y==0中，y为向量而0为标量。
# （1）可以通过np.vectorize()将函数向量化来进行计算
def f(x, y):
  if y == 0:
    return np.nan
  return x / y

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
f_vec = np.vectorize(f)
print(f_vec(df["a"], df["b"])) # [0.25 nan 0.5 ]
# （2）也可以使用@np.vectorize装饰器将函数向量化
@np.vectorize
def f(x, y):
  if y == 0:
    return np.nan
  return x / y

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
print(f(df["a"], df["b"])) # [0.25 nan 0.5 ]