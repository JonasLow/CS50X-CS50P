import cv2
import numpy as np

# Load the image
image = cv2.imread('bullet_hole_2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection to find bullet hole edges
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming the largest contour corresponds to the bullet hole
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    # Fit an ellipse to the bullet hole contour
    if len(largest_contour) >= 5:
        ellipse = cv2.fitEllipse(largest_contour)
        center, axes, angle = ellipse

        # Draw the ellipse on the original image
        cv2.ellipse(image, ellipse, (0, 255, 0), 2)

        # Calculate the angle relative to the glass surface
        angle_relative_to_glass = angle

        print(f"Angle relative to glass surface: {angle_relative_to_glass} degrees")

        # Display the image with the detected bullet hole
        cv2.imshow("Bullet Hole Analysis", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Not enough points to fit an ellipse.")

else:
    print("No bullet hole detected.")

