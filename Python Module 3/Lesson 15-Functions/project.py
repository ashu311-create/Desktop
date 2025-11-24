import math
def calculate_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.

  Args:
    radius: The radius of the circle (float).

  Returns:
    The circumference of the circle (float).
  """
  circumference = 2 * math.pi * radius
  return circumference
try:
  radius_input = float(input("Enter the radius of the circle: "))
  if radius_input < 0:
    print("Radius cannot be negative. Please enter a positive value.")
  else:
    circumference_result = calculate_circumference(radius_input)
    print(f"The circumference of the circle with radius {radius_input} is: {circumference_result:.2f}")
except ValueError:
  print("Invalid input. Please enter a numerical value for the radius.")