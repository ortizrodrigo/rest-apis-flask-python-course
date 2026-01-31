def add(x, y):
  return x + y

print(add(5, 7))
print((lambda x, y: x + y)(1, 2))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled, numbers)