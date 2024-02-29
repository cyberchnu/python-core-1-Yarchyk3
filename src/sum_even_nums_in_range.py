def sum_even_nums_in_range(start, stop):
  # Type your code
  sum_even = 0


  for num in range(start, stop):
    if num % 2 == 0:
      sum_even += num

  return sum_even
