user = {"username": "rodrigo", "access-level": "admin"}

def get_admin_password():
  return "1234"

def secure_get_admin_password():
  if user["access-level"] == "admin":
    return "1234"

print(get_admin_password())
print(secure_get_admin_password())

def make_secure(func):
  def secure_function():
    if user["access-level"] == "admin":
      return func()
    
  return secure_function
  
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
