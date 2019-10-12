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
  from math import log2
  f(b, a, 0, len(a))

a = [5, 1, 2, 7, 4, 3, 6]
sort(a)
print(a)