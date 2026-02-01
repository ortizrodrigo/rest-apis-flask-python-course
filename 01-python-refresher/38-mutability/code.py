a = []
b = a

b.append(32)

print(id(a), id(b))
print(a, b)

c = 10
d = 10

print(id(c), id(d))
