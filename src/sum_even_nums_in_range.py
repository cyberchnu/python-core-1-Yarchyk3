def sum_even_nums_in_range(start, stop):
  sum = 0
  for i in range(start,stop+1):
    if i % 2 == 0:
      sum += i
  return sum