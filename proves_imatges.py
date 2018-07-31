import cv2
import numpy as np
import imutils

imgfile = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_originals/DSIR5080.JPG'

img = cv2.imread(imgfile)

print(img.shape)
new_im = np.reshape(img,(img.shape[1],img.shape[0],img.shape[2]))
print(new_im.shape)
'''rows, cols, _ = img.shape
img = imutils.rotate(img,90)
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
img = cv2.warpAffine(img,M,(rows,cols))
print(img.shape)'''
save_path='proves/img.JPG'
cv2.imwrite(save_path,new_im)



