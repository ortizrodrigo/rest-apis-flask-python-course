import functools
user = {"username": "rodrigo", "access-level": "guest"}

def make_secure(access_level):
  def decorator(func):
    @functools.wraps(func) # keeps func's name and documentation
    def secure_function(*args, **kwargs):
      if user["access-level"] == access_level:
        return func(*args, **kwargs)
      else:
        return f"No {access_level} persmissions for {user['username']}"
      
    return secure_function
  return decorator

@make_secure("admin") # decorator
def get_admin_password():
  return "admin: 1234"
  
@make_secure("user")
def get_dashboard_password():
  return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = {"username": "rodrigo", "access-level": "admin"}

print(get_admin_password())
print(get_dashboard_password())