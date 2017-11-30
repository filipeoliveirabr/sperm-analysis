import cv2
import numpy as np

def filter_my_contours(image,contours):
    filtered_contours = []
    
    for i in contours:
        area = cv2.contourArea(i)
        if (area >= 2) and (area <= 500):
            filtered_contours.append(i)
            
    return filtered_contours

for x in range(1, 19):
    name  = "./resources/%d.tif" % (x)
    image = cv2.imread(name)
    image_orig = image.copy()
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ret , threshold = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3), np.uint8)
    threshold = cv2.bitwise_not(threshold)
    threshold = cv2.erode(threshold, kernel,iterations = 2)
    
    _,contours,_     = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = filter_my_contours(threshold, contours)
        
    title = "%d - sperm numbers %d" % (x, len(filtered_contours) )
    
    cv2.drawContours(image, filtered_contours, -1, (0, 200, 0), 2)
    file_path = './output/'+ title
    print(file_path) 
    
    cv2.imwrite(file_path + '.tif', image_orig)
#     cv2.imwrite(file_path + '_gray.tif', gray)
    cv2.imwrite(file_path + '_mark.tif', image)
    cv2.imwrite(file_path + '_th.tif', threshold)