import os
import numpy
#import cv2

annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/annotacions_crop'

'''imgpath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_girades'
im = cv2.imread(imgpath+'/DSIR5488.JPG')'''
#print('Shape',im.shape)
xmin1 = 10
xmax1 = xmin1
ymin1 = xmin1
ymax1 = ymin1
xmax1min = 10
ymax1min = 10	
for it, annofile in enumerate(os.listdir(annopath)):
	with open(os.path.join(annopath,annofile), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	print(len(annotations))
	
	annotation = []
	for itt, annot in enumerate(annotations):
		#print(annot)
		value = annot.split(' ')
		an = [float(e) for e in value if e is not '' ]
		annotation.append(an)
		if an[0]<xmin1:
			xmin1 = an[0]
			name1 = annofile
		if an[1]<ymin1:
			ymin1 = an[1]
			name2 = annofile
		if an[2]>xmax1:
			xmax1 = an[2]
			name3 = annofile
		if an[3]>ymax1:
			ymax1 = an[3]
			name4 = annofile
		if an[3]<ymax1min:
			ymax1min = an[3]
		if an[2]<xmax1min:
			xmax1min = an[2]



	print('Xmin = %.2f, Xmax = %.2f, Ymin = %.2f, Ymax = %.2f'%(xmin1, xmax1, ymin1, ymax1))

	
print('DEFINITIIVE!!\nXmin = %.2f, Xmax = %.2f, Ymin = %.2f, Ymax = %.2f'%(xmin1, xmax1, ymin1, ymax1))
print(xmax1min, ymax1min)