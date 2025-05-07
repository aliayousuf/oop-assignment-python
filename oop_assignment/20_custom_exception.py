
class InvalidAgeError(Exception):
  pass

def check_age(age):
  if age < 18:
    raise InvalidAgeError("Invalid age")
  print("Age is valid")

try:
  check_age(10)
except InvalidAgeError as e:
  print(f"Error: {e}")
