for m in range(1, 40):
  for n in range(1, m):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    if a + b + c == 1000:
      print(a, b, c)
      print(a * b * c)
