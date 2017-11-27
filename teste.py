import cv2
import numpy as np

def filter_my_contours(image,contours):
    filtered_contours = []
    
    for i in contours:
        
        area = cv2.contourArea(i)
        print(area)
        print(cv2.isContourConvex(i))
        
        if (area > 10):
            filtered_contours.append(i)
            
    return filtered_contours

image    = cv2.imread("./resources/19.tif")
gray     = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)



image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_range = np.array([0, 0, 180], dtype=np.uint8)
upper_range = np.array([150, 150, 255], dtype=np.uint8)
image = cv2.inRange(image, lower_range, upper_range)

cv2.imshow("title0", image)

# ret , threshold = cv2.threshold(gray,0, 255,cv2.THRESH_OTSU)
# kernel = np.ones((5,5), np.uint8)
# 
# cv2.imshow("Title1", threshold)
# cv2.imshow("Title2", threshold)

# _,contours,_     = cv2.findContours(threshold, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# filtered_contours = filter_my_contours(threshold, contours)
# 
# cv2.imshow("threshold", threshold)
# title = "Number %d" % (len(filtered_contours))
# cv2.drawContours(image, filtered_contours, -1, (0,200,0), 2)
# cv2.imshow(title, image)
#     
cv2.waitKey(0)