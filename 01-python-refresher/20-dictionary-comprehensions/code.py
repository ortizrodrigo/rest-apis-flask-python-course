users = [
  (0, "a", "password0"),
  (1, "b", "password1"),
  (2, "c", "password2"),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)