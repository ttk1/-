def sort(a):
  def f(a, b, s, t):
    if t <= 1:
      return
    n = t // 2
    m = t - n
    f(b, a, s, n)
    f(b, a, s + n, m)
    i = 0
    j = 0
    while True:
      if i == n and j == m:
        break
      elif i == n:
        b[s + i + j] = a[s + n + j]
        j += 1
      elif j == m:
        b[s + i + j] = a[s + i]
        i += 1
      else:
        if a[s + n + j] < a[s + i]:
          b[s + i + j] = a[s + n + j]
          j += 1
        else:
          b[s + i + j] = a[s + i]
          i += 1

  b = list(a)
  f(b, a, 0, len(a))


from random import random, seed
from benchmarker import Benchmarker
from copy import deepcopy

def random_list(max_length):
  return [random() for i in range(int(random() * max_length))]

'''
# ちゃんとソートされてるかチェックするぞ！
def check(x):
  if len(x) <= 1:
    return
  for i in range(len(x) - 1):
    if x[i] > x[i + 1]:
      raise Exception('ソートされてないぞ！')

for i in range(100):
  a = random_list(10000)
  sort(a)
  check(a)
'''

if __name__ == '__main__':
  seed(0)
  loop1 = [random_list(10000) for _ in range(100)]
  loop2 = deepcopy(loop1)
  with Benchmarker(width=20) as bench:
    @bench('builtin_sort')
    def _(bm):
      for a in loop1:
        a.sort()

    @bench('my_sort')
    def _(bm):
      for a in loop2:
        sort(a)

'''
# 結果...
# ビルトインのソートが圧倒的

## Matrix                 real    [01]    [02]
[01] builtin_sort       0.0520   100.0  4427.9
[02] my_sort            2.3026     2.3   100.0
'''
