from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle
import os
import numpy as np
import cv2

def vis_detections(im, annot):
    """Visual debugging of detections."""
    bbox = tuple(int(np.round(x)) for x in annot)
    flag = False
    for it,i in enumerate(bbox):
    	if i<1:
    		flag = True
    	if it == 2:
    		if i>im.shape[1]:
    			flag = True
    	if it == 3:
    		if i>im.shape[0]:
    			flag = True
    if flag:
    	cv2.rectangle(im, bbox[0:2], bbox[2:4], (0, 0, 204), 2)
    	print(bbox)
    else:
    	cv2.rectangle(im, bbox[0:2], bbox[2:4], (0, 204, 0), 2)
    return im

annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/anotacions_originals'
imagepath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_girades'
resultpath =  '../images_rndm_annot'

xmin_val = 100
ymin_val = 100
xmax_val = 100
ymax_val = 100
negative_file = []
superior_file = []
for it, annofile in enumerate(os.listdir(annopath)):
	filename = annofile.split('.txt')[0]
	
	with open(os.path.join(annopath,annofile), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	image = cv2.imread(os.path.join(imagepath,filename+'.JPG'))
	for annot in annotations:		
		value = annot.split(' ')
		annotation = [float(e) for e in value if e is not '' ]	
		if annotation[0]<1:
			xmin_val = annotation[0]
			negative_file.append(filename)
		if annotation[1]<1:
			ymin_val = annotation[1]
			negative_file.append(filename)
		if annotation[2]>image.shape[1]:
			xmax_val = annotation[2]
			superior_file.append(filename)
		if annotation[3]>image.shape[0]:
			ymax_val = annotation[3]
			superior_file.append(filename)

for filename in negative_file:
	with open(os.path.join(annopath,filename+'.txt'), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	image = cv2.imread(os.path.join(imagepath,filename+'.JPG'))
	print(filename)
	for annot in annotations:		
		value = annot.split(' ')
		annotation = [float(e) for e in value if e is not '' ]	
		image = vis_detections(image, annotation)
	if not os.path.exists(resultpath + 'negative/'):
		os.mkdir(resultpath + 'negative/')	
	savepath = resultpath + 'negative/' + filename + '_annot.JPG'	
	cv2.imwrite(savepath,image)
for filename in superior_file:
	with open(os.path.join(annopath,filename+'.txt'), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	image = cv2.imread(os.path.join(imagepath,filename+'.JPG'))
	print(filename)
	for annot in annotations:		
		value = annot.split(' ')
		annotation = [float(e) for e in value if e is not '' ]	
		image = vis_detections(image, annotation)
	if not os.path.exists(resultpath + 'superior/'):
		os.mkdir(resultpath + 'superior/')
	savepath = resultpath + 'superior/' + filename + '_annot.JPG'
	
	cv2.imwrite(savepath,image)
	

print("xmin",xmin_val)
print("ymin",ymin_val)
print("xmax",xmax_val)
print("ymax",ymax_val)
print("# of annot with not regular values",len(superior_file) + len(negative_file))