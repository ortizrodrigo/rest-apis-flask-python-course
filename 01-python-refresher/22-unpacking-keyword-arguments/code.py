def named(**kwargs):
  print(kwargs)

named(name="Bob", age=25)

# def post(url, data=None, json=None, **kwargs):
#   return request("post", url, data=data, json=json, **kwargs)