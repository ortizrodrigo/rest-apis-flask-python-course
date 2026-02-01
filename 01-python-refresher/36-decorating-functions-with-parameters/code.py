import functools
user = {"username": "rodrigo", "access-level": "guest"}



def make_secure(func):
  @functools.wraps(func) # keeps func's name and documentation
  def secure_function(*args, **kwargs):
    if user["access-level"] == "admin":
      return func(*args, **kwargs)
    else:
      return f"No admin persmissions for {user['username']}"
    
  return secure_function

@make_secure # decorator
def get_admin_password(panel):
  if panel == "admin":
    return "1234"
  elif panel == "billing":
    return "super_secure_password"
  
print(get_admin_password("billing"))



