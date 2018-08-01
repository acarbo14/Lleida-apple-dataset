import os
import random
from random import shuffle


filespath = '/work/acarbo/faster_rcnn/data/lleida_dataset/dataset/imatges'
save_path = '/work/acarbo/faster_rcnn/data/lleida_dataset/dataset/sets'

if not os.path.exists(save_path):
	os.mkdir(save_path)

filenames = [file.split('.')[0] for file in os.listdir(filespath)]
for a in range(3):
	print(filenames[a])
files = random.sample(filenames,len(filenames))
first_split = int(len(files)*0.6)
second_split = int(len(files)*0.2)
train_set = files[0:first_split]
val_set = files[first_split:first_split + second_split]
test_set = files[first_split + second_split : first_split + 2*second_split]
trainval_set = files[0:first_split + second_split]


print('Train:',len(train_set))
print('Validation:',len(val_set))
print('Test:',len(test_set))
print('Trainval:',len(trainval_set))

with open(os.path.join(save_path,'train.txt'),'w') as f:
	[f.write(file+'\n') for file in train_set]

with open(os.path.join(save_path,'val.txt'),'w') as f:
	[f.write(file+'\n') for file in val_set]

with open(os.path.join(save_path,'test.txt'),'w') as f:
	[f.write(file+'\n') for file in test_set]	

with open(os.path.join(save_path,'trainval.txt'),'w') as f:
	[f.write(file+'\n') for file in trainval_set]

with open(os.path.join(save_path,'all.txt'),'w') as f:
	[f.write(file+'\n') for file in files]