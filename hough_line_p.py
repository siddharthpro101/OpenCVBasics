import cv2 as cv
import numpy as np
img=cv.imread("C:/Users/Turing/Downloads/road.jpeg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

edges=cv.Canny(gray,255,255,apertureSize=3)
cv.imshow("Image",edges)

lines=cv.HoughLinesP(edges,1,np.pi/180,100,
                     minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow("Imae",img)
cv.waitKey(0)
cv.destroyAllWindows()

