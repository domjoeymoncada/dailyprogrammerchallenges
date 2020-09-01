from math import floor

hex_base = \
(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  'A', 'B', 'C', 'D', 'E', 'F'
)

def decimal_to_hex(decimal: int) -> str:
  if 0 <= decimal <= 255:
    current_int = decimal
    hex_string = ''

    if decimal == 0:
      hex_string += '00'
    else:
      while current_int != 0:
        hex_string += str(hex_base[(current_int%16)])
        current_int = floor(current_int / 16)
    
    return hex_string[::-1]

def hexcolor(rgb: list) -> str:
  hexstring = '#'

  try:
    for num in rgb:
      hex_value = decimal_to_hex(num)

      if len(hex_value) < 2:
        hex_value = '0' + hex_value
      hexstring += hex_value
  except TypeError:
    hexstring = "You inputted an invalid number!"
  
  return hexstring

print(hexcolor([255, 99, 71]))