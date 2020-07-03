import re

def balanced(xy_string: str) -> bool:
  x_instances = re.findall('x', xy_string)
  remaining_chars = len(xy_string) - len(x_instances)

  return True if len(x_instances) == remaining_chars else False

is_balanced = balanced('')
print(is_balanced)