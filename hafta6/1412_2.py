import cv2    #pip install opencv-python
import numpy as np
resim=cv2.imread("hafta6/cocuklar.jpg")
h,w,d=resim.shape
print(h,w,d)
piksel=resim[135:400,100:280]
#resim[80:250,300:500]=piksel
# cv2.imshow("test",resim)
# cv2.waitKey(0)
img=np.zeros((500,500,3),np.uint8)
cv2.line(img,(0,0),(100,500),(0,200,200),4)
cv2.circle(img,(400,300),60,(0,200,200),5)
cv2.imshow("test",img)
cv2.waitKey(0)









