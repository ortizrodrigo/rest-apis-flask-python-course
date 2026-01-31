numbers = [1, 2, 3]

print([num**2 for num in numbers])

friends = ["a", "b", "c"]

for friend in friends:
  if friend.startswith("a"):
    print(friend)

print([friend for friend in friends if friend.startswith("a")])
