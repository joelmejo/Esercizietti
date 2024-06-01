from math import log10, floor
def int_to_roman(n: int) -> str:
  if n > 3999:
    return
  roman_number = ""
  roman_symbols = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]] 
  roman_symbols.reverse()
  for symbol, value in roman_symbols:
    symbol_count = n // value
    if value - n < 10 ** floor(log10(max(1, value - 1))):
      for symbol2, value in roman_symbols:
        if value == 10 ** floor(log10(max(1, value - 1))):
          roman_number += symbol2
        roman_number += symbol
    roman_number += symbol * symbol_count
    n %= value
  print(roman_number)

int_to_roman(4)
      
      
      
      
    