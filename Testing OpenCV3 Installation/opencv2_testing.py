import cv2
image = cv2.imread("clouds.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
y = cv2.imshow("Over the Clouds", image)
x = cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyWindow("Over the Clouds")
cv2.destroyWindow("Over the Clouds - gray")
