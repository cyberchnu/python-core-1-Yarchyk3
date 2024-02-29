def mean(number):
  # Type your code
    number_str = str(number)

    sum_of_digits = 0
    count_of_digits = 0

    for digit in number_str:

        if digit.isdigit():
            sum_of_digits += int(digit)
            count_of_digits += 1


    if count_of_digits > 0:
        mean_value = sum_of_digits / count_of_digits
        return mean_value
    else:
        return 0