import cv2
import numpy as np

def filter_my_contours(image,contours):
    filtered_contours = []
    
    ImageArea = image.shape[0] * image.shape[1]
    for i in contours:
        
        area = cv2.contourArea(i)
        print( area )
        if (area >= 200) and (area <= 999):
            filtered_contours.append(i)
            
    return filtered_contours

for x in range(10, 20):
    name = "./resources/%d.tif" % (x)
    
    image    = cv2.imread(name)
    
    blurred  = cv2.pyrMeanShiftFiltering(image,0,3)
    gray     = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    ret , threshold = cv2.threshold(gray,255, 255,cv2.THRESH_OTSU)
    masked_image   = cv2.bitwise_and(image,image,mask = threshold)
    
    _,contours,_     = cv2.findContours(threshold, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = filter_my_contours(threshold, contours)
    
    title = "Number %d Image %d  " % (len(filtered_contours), x)
    
    cv2.drawContours(image, filtered_contours, -1, (0,200,0), 2)
    cv2.imshow(title, image)
    
cv2.waitKey(0)