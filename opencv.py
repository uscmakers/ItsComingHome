import numpy as np
import matplotlib.pyplot as plt
import cv2

# # read the image
# image = cv2.imread("monitor.jpg")

# # convert to grayscale
# grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # perform edge detection
# edges = cv2.Canny(grayscale, 30, 100)

# # detect lines in the image using hough lines technique
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)

# # iterate over the output lines and draw them
# for line in lines:
#     for x1, y1, x2, y2 in line:
#         cv2.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)

# # show the image
# plt.imshow(image)
# plt.show()

#detect lines/edges in live camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _, image = cap.read()
    # convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # perform edge detection
    edges = cv2.Canny(grayscale, 30, 100)
    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # show images
    cv2.imshow("image", image)
    cv2.imshow("edges", edges)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

#detecting circles 
# load the image
# img = cv2.imread("coins.jpg")

# # convert BGR to RGB to be suitable for showing using matplotlib library
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # make a copy of the original image
# cimg = img.copy()

# # convert image to grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # apply a blur using the median filter
# img = cv2.medianBlur(img, 5)

# # finds the circles in the grayscale image using the Hough transform
# circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, minDist=80, param1=110, param2=39, maxRadius=70)

# for co, i in enumerate(circles[0, :], start=1):
#     # draw the outer circle in green
#     cv2.circle(cimg,(int(i[0]),int(i[1])),int(i[2]),(0,255,0),2)
#     # draw the center of the circle in red
#     cv2.circle(cimg,(int(i[0]),int(i[1])),2,(0,0,255),3)
    
# # print the number of circles detected
# print("Number of circles detected:", co)
# #save the image, convert to BGR to save with proper colors
# cv2.imwrite("coins_circles_detected.png", cimg)
# # show the image
# plt.imshow(cimg)
# plt.show()
