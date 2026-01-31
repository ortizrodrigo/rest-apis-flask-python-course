def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cannot be 0")
  return dividend / divisor

# divide(15, 0)

grades = [2]

try:
  average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
  print(e)
  print("There are no grades in your list")
else:
  print(f"The avg grade is {average}")
finally:
  print("Thanks!")