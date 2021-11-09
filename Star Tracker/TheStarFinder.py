import cv2
import matplotlib.pyplot as plt
import math
import numpy as np


image= cv2.imread('Orion_Lower.png')
original_image= image
h,w,c = image.shape

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
threshhold, destination = cv2.threshold(gray,100,250,cv2.THRESH_BINARY)
edges= cv2.Canny(destination, 100,200)

contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
Stars = []
PilotStars = []
Triangles = []

for (i,c) in enumerate(sorted_contours):
    M= cv2.moments(c)
    #cx= int(M['m10']/M['m00'])
    #cy= int(M['m01']/M['m00'])
    
    (x,y),radius = cv2.minEnclosingCircle(c)
    x=int(x)
    y=int(y)
    radius = int(radius)
    StarArea = 3.1415 * radius * radius
    #cv2.putText(image, text= str(i+1), org=(x,y),
            #fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),
            #thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(image,(x,y),radius,(255,0,0),1)
    StarNumber = i+1
    Stars.append(StarNumber)
    Stars.append(StarArea)
    Stars.append(x)
    Stars.append(y)

PilotStars = Stars[:16]
cv2.line(image,(PilotStars[2],PilotStars[3]),(PilotStars[6],PilotStars[7]),(0,0,255),1)
Length1 = cv2.norm((PilotStars[2],PilotStars[3]),(PilotStars[6],PilotStars[7]))
cv2.putText(image, text = str(Length1), org = (PilotStars[6],PilotStars[7]), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),
            thickness=1, lineType=cv2.LINE_AA)

cv2.line(image,(PilotStars[6],PilotStars[7]),(PilotStars[10],PilotStars[11]),(0,0,255),1)
Length2 = cv2.norm((PilotStars[6],PilotStars[7]),(PilotStars[10],PilotStars[11]))
cv2.putText(image, text = str(Length2), org = (PilotStars[10],PilotStars[11]), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),
            thickness=1, lineType=cv2.LINE_AA)

cv2.line(image,(PilotStars[10],PilotStars[11]),(PilotStars[2],PilotStars[3]),(0,0,255),1)
Length3 = cv2.norm((PilotStars[10],PilotStars[11]),(PilotStars[2],PilotStars[3]))
cv2.putText(image, text = str(Length3), org = (PilotStars[2],PilotStars[3]), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),
            thickness=1, lineType=cv2.LINE_AA)

Triangles.append(Length1)
Triangles.append(Length2)
Triangles.append(Length3)

#Heron's formula for area of triangle
perimeter = (Length1+Length2+Length3)/2
#value = (Length1**2 - Length2**2 + Length3**2)/(-2*Length2 * Length3)
area = math.sqrt(perimeter*(perimeter-Length1)*(perimeter-Length2)*(perimeter-Length3))

#Finding coordinates of centroid
centroid_x = (PilotStars[2]+PilotStars[6]+PilotStars[10])/3
centroid_y = (PilotStars[3]+PilotStars[7]+PilotStars[11])/3


# cv2.line(image,(PilotStars[2],PilotStars[3]),(PilotStars[18],PilotStars[19]),(0,0,255),3)
# Length4 = cv2.norm((PilotStars[2],PilotStars[3]),(PilotStars[18],PilotStars[19]))
# cv2.putText(image, text = str(Length4), org = (PilotStars[18],PilotStars[19]), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),
#             thickness=2, lineType=cv2.LINE_AA)

#draw crossheirs 
avgh = h/2
int(avgh)
avgw = w/2
int(avgw)
cv2.line(image,(0,int(avgh)),(w,int(avgh)), (100,100,100), 1)
cv2.line(image,(int(avgw),0),(int(avgw),h), (100,100,100), 1)

#Draw line from crossheirs to centroid
cv2.line(image, (int(avgw),int(avgh)), (int(centroid_x),int(centroid_y)),(50,200,200),1)
Length4 = cv2.norm((int(avgw),int(avgh)),(int(centroid_x),int(centroid_y)))

#determine angle from this line to the x axis of camera
Length5 = cv2.norm((int(avgw),int(avgh)),(int(centroid_x),int(avgh)))
phi = np.arccos(Length5/Length4)

#determine angle (in rad) from camera pointing vector to centroid of triangle
r = 10000 #assume r is large relative to length4 bc celestial sphere
step1 = ((r*r) + (r*r) - (Length4*Length4)) / (2*r*r)
theta = np.arccos(step1)

#find relative declination gamma using r_dec
r_dec = np.abs(avgh-centroid_x)
gamma = np.arccos(((r*r) + (r*r) - (r_dec*r_dec)) / (2*r*r))


plt.imshow(image)
plt.show()
