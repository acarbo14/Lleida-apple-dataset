from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import numpy as np
import pandas as pd
import shutil
import PIL
from PIL import Image
import pdb
from lxml import etree as ET




path = '/work/acarbo/faster_rcnn/data/lleida_dataset/dataset/annotations'
Files = os.listdir(path)
save_dir = '/work/acarbo/faster_rcnn/data/lleida_dataset/dataset/annotations_xml'
print("Writing on folder: %s"%save_dir)
img_dir = '/work/acarbo/faster_rcnn/data/lleida_dataset/dataset/imatges'
if os.path.exists(save_dir):
	shutil.rmtree(save_dir)	
	os.makedirs(save_dir)
else:	
	os.makedirs(save_dir)

for file in Files:
	#full_filename = os.path.join(path,file)
	filename = file.split(".txt")[0]
	width = PIL.Image.open(os.path.join(img_dir,filename + ".JPG")).size[0]
	height = PIL.Image.open(os.path.join(img_dir,filename + ".JPG")).size[1]
	with open(os.path.join(path,file), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	f = ET.Element("annotations")
	ET.SubElement(f,'filename').text = filename + ".JPG"
	thesize = ET.SubElement(f,'size')
	ET.SubElement(thesize,'width').text = str(width)
	ET.SubElement(thesize,'height').text = str(height)
	ET.SubElement(thesize,'depth').text = "3"
	for annot in annotations:
		value = annot.split(' ')
		annotation = [float(e) for e in value if e is not '' ]
		xmin = annotation[0]
		ymin = annotation[1]
		xmax = annotation[2]
		ymax = annotation[3]
		obj = ET.SubElement(f,'object')
		ET.SubElement(obj,'name').text = "Poma"
		ET.SubElement(obj,'difficult').text = "0"
		bbox = ET.SubElement(obj,'bbox')
		xmin_xml = ET.SubElement(bbox,'xmin')		
		ymin_xml = ET.SubElement(bbox,'ymin')
		xmax_xml = ET.SubElement(bbox,'xmax')
		ymax_xml = ET.SubElement(bbox,'ymax')		
		xmin_xml.text = str(int(xmin))
		xmax_xml.text = str(int(xmax))
		ymin_xml.text = str(int(ymin))
		ymax_xml.text = str(int(ymax))

	savexml = os.path.join(save_dir, filename + ".xml")
	tree = ET.ElementTree(f)
	
	tree.write(savexml, pretty_print = True)