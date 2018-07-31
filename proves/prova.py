import os
import numpy as np

import shutil
def crop_annot(annot,start_hor,start_ver,end_hor,end_ver):
	crop_annot = []
	for ii in range(len(annot)):
		#Primer s'ha de comprovar que xmin>st_hor i <end_hor
		#Si ok comprovem
		xmin = annot[ii][0]
		ymin = annot[ii][1]
		xmax = annot[ii][2]
		ymax = annot[ii][3]
		if xmin >= start_hor and xmin < end_hor:
			if ymax >= start_ver and ymax < end_ver:
				annot[ii][0] = annot[ii][0] - start_hor
				annot[ii][2] = annot[ii][2] - start_hor
				annot[ii][1] = annot[ii][1] - start_ver
				annot[ii][3] = annot[ii][3] - start_ver
				
				crop_annot.append(annot[ii])
			elif ymin >= start_ver and ymin < end_ver:
				annot[ii][0] = annot[ii][0] - start_hor
				annot[ii][2] = annot[ii][2] - start_hor
				annot[ii][1] = annot[ii][1] - start_ver
				annot[ii][3] = annot[ii][3] - start_ver
				
				crop_annot.append(annot[ii])
		elif xmax >= start_hor and xmax < end_hor:
			if ymax >= start_ver and ymax < end_ver:
				annot[ii][0] = annot[ii][0] - start_hor
				annot[ii][2] = annot[ii][2] - start_hor
				annot[ii][1] = annot[ii][1] - start_ver
				annot[ii][3] = annot[ii][3] - start_ver
				
				crop_annot.append(annot[ii])
			elif ymin >= start_ver and ymin < end_ver:
				annot[ii][0] = annot[ii][0] - start_hor
				annot[ii][2] = annot[ii][2] - start_hor
				annot[ii][1] = annot[ii][1] - start_ver
				annot[ii][3] = annot[ii][3] - start_ver
				
				crop_annot.append(annot[ii])

	return crop_annot
annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/anotacions_originals/DSIR5088.txt'

with open(os.path.join(annopath), 'r') as f:
	lines = f.readlines()
	annotations = [x.strip() for x in lines]
annotation = []
for annot in annotations:
	#print(annot)
	value = annot.split(' ')
	an = [float(e) for e in value if e is not '' ]
	if an[0] < 0:
		an[0] = 0
		print('EEEEEH que passa3')
	if an[1] < 0:
		an[1] = 0
		print('EEEEEH que passa2')
	if an[2] > 2304:
		an[2] = 2304-1
		print('EEEEEH que passa1')
	if an[3] > 1536:
		an[3] = 1536 - 1
		print('EEEEEH que passa')
	annotation.append(an)

start_hor = 0
start_ver = 352
end_hor = 672
end_ver = 832
hor_size = 672
ver_size = 480
new_annot = crop_annot(annotation,start_hor,start_ver,end_hor,end_ver)


for i in range(len(new_annot)):
	if new_annot[i][0]<0:
		print('holi')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])					
	if new_annot[i][1]<0:
		print('holi2')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])
		
	if new_annot[i][2] > hor_size:
		print('holi3')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])
		
	if new_annot[i][3] > ver_size:
		print('holi4')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])
	if new_annot[i][2] < new_annot[i][0] or new_annot[i][2] < 0:
		print('holi5')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])
	if new_annot[i][3] < new_annot[i][1] or new_annot[i][3] < 0:
		print('holi6')
		
		print(start_hor,start_ver,end_hor,end_ver)
		print(new_annot[i])		
print(crop_annot)	
			
	