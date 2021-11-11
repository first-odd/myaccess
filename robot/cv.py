import numpy as np
import cv2

rgb = cv2.imread('/Users/jacksonandrew/Desktop/pho.JPG')
print(rgb)
print(rgb.shape) #3维：彩色RGB
def show_img(x):
    cv2.imshow('image',x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



grayscale = cv2.imread('/Users/jacksonandrew/Desktop/pho.JPG',cv2.IMREAD_GRAYSCALE) #灰度图
#cv2.imwrite('huidu.png',grayscale)保存灰度图
show_img(grayscale)