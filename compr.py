import os
import cv2
import numpy as np


def vis_detections(im, annot):
    """Visual debugging of detections."""
    bbox = tuple(int(np.round(x)) for x in annot)        
    cv2.rectangle(im, bbox[0:2], bbox[2:4], (0, 204, 0), 2)
    
    return im

#imagepath = '/work/acarbo/faster_rcnn/data/underwood_dataset/apples/images/20130320T013608.056531_21.png'
imagepath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_girades/DSIR5468.JPG'
annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/anotacions_originals/DSIR5172.txt'
results = 'images_proves/rotated2-DSIR5172.JPG'

image = cv2.imread(imagepath)
print(image.shape)
'''with open(annopath, 'r') as f:
	lines = f.readlines()
	annotations = [x.strip() for x in lines]

print(image.shape)
for annot in annotations:
	#print(annot)
	value = annot.split(' ')
	annotation = [float(e) for e in value if e is not '' ]
	image = vis_detections(image, annotation)
	cv2.imwrite(results, image)'''


