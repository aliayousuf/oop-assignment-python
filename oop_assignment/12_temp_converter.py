
class TemperatureConverter:

  @staticmethod
  def celsius_to_fahrenheit(c):
    return (c *9/5)+32

f = TemperatureConverter()
print(f"{f.celsius_to_fahrenheit(37)}F")
