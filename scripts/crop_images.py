import os
import numpy as np
import cv2
import shutil

def crop_annot(annot,start_hor,start_ver,end_hor,end_ver, hor_size, ver_size):
	crop_annot = []
	for ii in range(len(annot)):		
		xmin = annot[ii][0]
		ymin = annot[ii][1]
		xmax = annot[ii][2]
		ymax = annot[ii][3]
		if xmin >= start_hor and xmin < end_hor:
			if ymax >= start_ver and ymax < end_ver:
				Xmin = annot[ii][0] - start_hor
				Ymin = annot[ii][1] - start_ver
				Xmax = annot[ii][2] - start_hor
				Ymax = annot[ii][3] - start_ver
				if Xmin < 0:
					Xmin = 0
				if int(Xmin)==hor_size -1:
					Xmin = Xmin -1
				if Ymin < 0:
					Ymin = 0
				if int(Ymin)==ver_size - 1:
					Ymin -= 1
				if Xmax >= hor_size:
					Xmax = hor_size - 1
				if Ymax >= ver_size:
					Ymax = ver_size - 1
				crop_annot.append([Xmin, Ymin, Xmax, Ymax])
			elif ymin >= start_ver and ymin < end_ver:
				Xmin = annot[ii][0] - start_hor
				Ymin = annot[ii][1] - start_ver
				Xmax = annot[ii][2] - start_hor
				Ymax = annot[ii][3] - start_ver
				if Xmin < 0:
					Xmin = 0
				if int(Xmin)==hor_size -1:
					Xmin = Xmin -1
				if Ymin < 0:
					Ymin = 0
				if int(Ymin)==ver_size - 1:
					Ymin -= 1
				if Xmax >= hor_size:
					Xmax = hor_size - 1
				if Ymax >= ver_size:
					Ymax = ver_size - 1
				crop_annot.append([Xmin, Ymin, Xmax, Ymax])
		elif xmax >= start_hor and xmax < end_hor:
			if ymax >= start_ver and ymax < end_ver:
				Xmin = annot[ii][0] - start_hor
				Ymin = annot[ii][1] - start_ver
				Xmax = annot[ii][2] - start_hor
				Ymax = annot[ii][3] - start_ver
				if Xmin < 0:
					Xmin = 0
				if int(Xmin)==hor_size -1:
					Xmin = Xmin -1
				if Ymin < 0:
					Ymin = 0
				if int(Ymin)==ver_size - 1:
					Ymin -= 1
				if Xmax >= hor_size:
					Xmax = hor_size - 1
				if Ymax >= ver_size:
					Ymax = ver_size - 1
				crop_annot.append([Xmin, Ymin, Xmax, Ymax])
			elif ymin >= start_ver and ymin < end_ver:
				Xmin = annot[ii][0] - start_hor
				Ymin = annot[ii][1] - start_ver
				Xmax = annot[ii][2] - start_hor
				Ymax = annot[ii][3] - start_ver
				if Xmin < 0:
					Xmin = 0
				if int(Xmin)==hor_size -1:
					Xmin = Xmin -1
				if Ymin < 0:
					Ymin = 0
				if int(Ymin)==ver_size - 1:
					Ymin -= 1
				if Xmax >= hor_size:
					Xmax = hor_size - 1
				if Ymax >= ver_size:
					Ymax = ver_size - 1
				crop_annot.append([Xmin, Ymin, Xmax, Ymax])
	return crop_annot

debug = False
imgpath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_girades'
savepath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_crop'
annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/anotacions_originals'
new_annopath ='/work/acarbo/faster_rcnn/data/lleida_dataset/annotacions_crop'

hor_size = 672
ver_size = 480
overlap = 128
if not os.path.exists(savepath):
	os.mkdir(savepath)
else:
	shutil.rmtree(savepath)
	os.mkdir(savepath)
if not os.path.exists(new_annopath):
	os.mkdir(new_annopath)
else:
	shutil.rmtree(new_annopath)
	os.mkdir(new_annopath)

for file in os.listdir(imgpath):
	filename = file.split('.')[0]
	img = cv2.imread(imgpath + '/' + filename + '.JPG')
	print(img.shape[0])
	steps = (img.shape[0]-overlap)/(ver_size-overlap)
	
	with open(os.path.join(annopath,filename + '.txt'), 'r') as f:
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
		if an[2] > img.shape[1]:
			an[2] = img.shape[1] - 1
			print('EEEEEH que passa1')
		if an[3] > img.shape[0]:
			an[3] = img.shape[0] - 1
			print('EEEEEH que passa')
		annotation.append(an)
	it = 0
	for yy in range(int(steps)):
		if yy == 0:
			start_ver = yy*ver_size
			end_ver = ver_size
		else:
			start_ver = end_ver - overlap
			end_ver = start_ver + ver_size

		for xx in range(int(steps)):
			if xx == 0:			
				start_hor = xx*hor_size
				end_hor = hor_size	
			else:			
				start_hor = end_hor - overlap
				end_hor = start_hor + hor_size

			new_img = img[start_ver : end_ver, start_hor : end_hor,:]
			new_filename = filename + '_' + str(it + 1)
			cv2.imwrite(os.path.join(savepath,new_filename + '.JPG'),new_img)			
			new_annot = crop_annot(annotation,start_hor,start_ver,end_hor,end_ver,hor_size,ver_size)

			for i in range(len(new_annot)):
				if new_annot[i][0]<0:
					print('holi')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])					
				if new_annot[i][1]<0:
					print('holi2')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])
					
				if new_annot[i][2] > hor_size:
					print('holi3')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])
					
				if new_annot[i][3] > ver_size:
					print('holi4')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])
				if new_annot[i][2] < new_annot[i][0] or new_annot[i][2] < 0:
					print('holi5')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])
					debug = True
				if new_annot[i][3] < new_annot[i][1] or new_annot[i][3] < 0:
					print('holi6')
					print(new_filename)
					print(start_hor,start_ver,end_hor,end_ver)
					print(new_annot[i])
					debug = True
			it += 1		
			print(start_hor,start_ver,end_hor,end_ver)
			with open(os.path.join(new_annopath, new_filename + '.txt'),'w') as f:				
				for ite in range(len(new_annot)):
					f.write('%.2f %.2f %.2f %.2f\n'%(new_annot[ite][0], new_annot[ite][1], new_annot[ite][2], new_annot[ite][3]))

			if debug:
				break
		if debug:
			break
	if debug:
		break

	print(it)

print(len(os.listdir(savepath)))