friend_ages = {"Rodrigo": 22, "Old Bob": 10000, "Some guy": 18}

friend_ages["Old Bob"] *= 2

print(friend_ages)

for friend, age in friend_ages.items():
  print(f"{friend} is {age} years old")