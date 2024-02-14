########################## libraries ##########################
import cv2 as cv 
import math 

######################## Click Points #########################

img = cv.imread("D:/Seivan's Workshop/Opencv Projects/Angle Measurment/pics/angle3.jpg")


points=[]

def click_points(event,x,y,flag,params):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x,y])
        cv.circle(img, (x,y), 5, (255,0,0),-1)


############################ Slope ############################

def slope(pts1,pts2):
    
    x1 , y1 = pts1[0] , pts1[1]
    x2 , y2 = pts2[0] , pts2[1]
    
    e = 0.000001
    slope = (y2-y1 + e)/(x2-x1 + e)
    return slope

######################## Angle Finder #########################

def angle_measure(points):
    
    pts1 , pts2 , pts3 = points[-3:]
    
    slope1 = slope(pts1,pts2)
    slope2 = slope(pts2,pts3)

    angleR = math.atan( (slope1 - slope2)/(1+slope1*slope2)  )
    angle = abs(round(math.degrees(angleR)))
    
    cv.putText(img, str(angle), (pts2[0]-50 , pts2[1]-50), cv.FONT_HERSHEY_PLAIN, 2, (0,0,0), thickness=2)
    


######################## imshow loop ##########################

while True:
    cv.imshow("imgae",img)
    cv.setMouseCallback("imgae", click_points)
    
    if len(points) %3 == 0 and len(points) != 0 :
        angle_measure(points)
        
        pts1,pts2,pts3 = points[-3:]
        
        cv.line(img, pts1, pts2, (0,0,255) , thickness=3)
        cv.line(img, pts2, pts3, (0,0,255) , thickness=3)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
    if cv.waitKey(1) & 0xFF == ord("r"):
        points = []
        img = cv.imread("D:/Seivan's Workshop/Opencv Projects/Angle Measurment/pics/angle3.jpg")
    
    
cv.destroyAllWindows()













