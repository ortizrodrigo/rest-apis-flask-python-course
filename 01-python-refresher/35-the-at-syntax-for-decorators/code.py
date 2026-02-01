import functools
user = {"username": "rodrigo", "access-level": "guest"}



def make_secure(func):
  @functools.wraps(func) # keeps func's name and documentation
  def secure_function():
    if user["access-level"] == "admin":
      return func()
    else:
      return f"No admin persmissions for {user['username']}"
    
  return secure_function

@make_secure # decorator
def get_admin_password():
  return "1234"
  
print(get_admin_password())
print(get_admin_password.__name__)


