some_iterable = [(1, 2, 3), (1, 2, 3), (1, 2, 3)]

for one, two, three in some_iterable:
  print(one, two, three)

head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

head, *tail = {1, 2, 3, 4, 5}
print(head, tail)

*head, tail = {1, 2, 3, 4, 5}
print(head, tail)