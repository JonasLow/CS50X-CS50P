import cv2
import numpy as np

def measure_bullet_angle(image):
  """Measures the angle at which a bullet was fired through glass.

  Args:
    image: A numpy array representing the image of the bullet hole in glass.

  Returns:
    A float representing the angle at which the bullet was fired, in degrees.
  """

  # Convert the image to grayscale.
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Find the edges of the bullet hole.
  edges = cv2.Canny(gray, 50, 150)

  # Find the contours of the bullet hole.
  contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Find the largest contour.
  largest_contour = max(contours, key=cv2.contourArea)

  # Find the center of the bullet hole.
  center = cv2.moments(largest_contour)['m10'] / cv2.moments(largest_contour)['m00']

  # Find the angle of the bullet hole.
  angle = cv2.phase(center[0], center[1], np.array([0, 0]))

  return angle

# Load the image of the bullet hole in glass.
image = cv2.imread("bullet_hole.jpg")

# Measure the angle at which the bullet was fired.
angle = measure_bullet_angle(image)

# Print the angle.
print("The angle at which the bullet was fired is:", angle, "degrees.")