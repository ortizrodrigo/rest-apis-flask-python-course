friends = {"Rodrigo", "Joe", "Bob"}
abroad = {"Rodrigo", "Charlie"}

local_friends = friends.difference(abroad)
print(local_friends, abroad.difference(friends))

all_friends = friends.union(abroad)
print(all_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both_disciplines = art.intersection(science)
print(both_disciplines)