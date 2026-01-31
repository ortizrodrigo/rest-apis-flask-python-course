def multiply(*args):
  print(args)
  total = 1
  for arg in args:
    total *= arg
  return total

print(multiply(1, 3, 4))

def add(x, y):
  return x + y

nums = {"x": 1, "y": 2}
print(add(**nums))

def apply(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return add(args[:2])
  else:
    return "meh"
  
print(apply(1, 2, 3, 4, 5, 6, operator="*"))