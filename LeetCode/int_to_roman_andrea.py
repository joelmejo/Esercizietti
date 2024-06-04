from math import floor, log10


def int_to_roman(n: int) -> str:
  roman_numbers = {
      1: "I",
      5: "V",
      10: "X",
      50: "L",
      100: "C",
      500: "D",
      1000: "M"
  }
  result = ""
  for value, symbol in reversed(roman_numbers.items()):
    count = n // value
    if count > 0:
      result += symbol * count
      n %= value
    power_of_ten = 10**floor(log10(max(1, value - 1)))
    if n == 0:
      break
    if 0 <= (value - 1) - n <= power_of_ten - 1:
      result += roman_numbers[power_of_ten]
      result += symbol
      n -= value - power_of_ten
  return result


print(int_to_roman(34))