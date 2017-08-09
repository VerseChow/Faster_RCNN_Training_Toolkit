#!/usr/bin/env python
import os
import cv2
from lxml import etree

label2name = {
'0':'tide',
'1':'spray_bottle_a',
'2':'waterpot',
'3':'sugar',
'4':'red_bowl',
'5':'clorox',
'6':'shampoo',
'7':'downy',
'8':'salt',
'9':'toy', 
'10':'detergent', 
'11':'scotch_brite',
'12':'cola',
'13':'blue_cup',
'14':'ranch',
'15':'__background__'
}

def read_label(label_file):
	label = {}	
	with open(label_file, 'r') as f:
		lines = f.readlines()
		for line in lines:
			seqs = line[:-1].split()
			label[seqs[0]] = seqs[1]
		#print label

	with open('/home/sui/workspace/cnn_data/progress/ImageSets/Main/test.txt', 'w') as out:
	#with open('/home/sui/workspace/cnn_data/progress/ImageSets/Main/train.txt', 'w') as out:
		for f in label.keys():
			if label[f] != '15':
				file_name = f[:f.find('.')] + '\n'
				out.write(file_name)
		
	return label

def process_one_folder(input_directory, label):
	for file_name in os.listdir(input_directory):
		if label[file_name] != '15':
			print file_name 
			xml_file_name = file_name[:file_name.find('.')] + '.xml'
			with open('/home/sui/workspace/cnn_data/progress/Annotations/' + xml_file_name, 'w') as out:
				img = cv2.imread(input_directory + file_name)
				print img.shape

				root = etree.Element('annotation')
				chd_folder = etree.Element('folder')
				chd_folder.text = 'progress'
				root.append(chd_folder)
				chd_fname = etree.Element('filename')
				chd_fname.text = file_name
				root.append(chd_fname)

				chd_size = etree.Element('size')
				chd_size_width = etree.Element('width')
				chd_size_width.text = str(img.shape[1])	
				chd_size_height = etree.Element('height')
				chd_size_height.text = str(img.shape[0])
				chd_size_depth = etree.Element('depth')
				chd_size_depth.text = str(img.shape[2])
				chd_size.append(chd_size_width)
				chd_size.append(chd_size_height)
				chd_size.append(chd_size_depth)			
				root.append(chd_size)

				chd_obj = etree.Element('object')
				chd_obj_name = etree.Element('name')
				chd_obj_name.text = label2name[label[file_name]] 
				chd_obj.append(chd_obj_name)
				chd_obj_bbox = etree.Element('bndbox')
				chd_obj_bbox_xmin = etree.Element('xmin')	
				chd_obj_bbox_xmin.text = '1'
				chd_obj_bbox.append(chd_obj_bbox_xmin)
				chd_obj_bbox_ymin = etree.Element('ymin')	
				chd_obj_bbox_ymin.text = '1'
				chd_obj_bbox.append(chd_obj_bbox_ymin)
				chd_obj_bbox_xmax = etree.Element('xmax')	
				chd_obj_bbox_xmax.text = str(img.shape[1])	
				chd_obj_bbox.append(chd_obj_bbox_xmax)
				chd_obj_bbox_ymax = etree.Element('ymax')	
				chd_obj_bbox_ymax.text = str(img.shape[0])	
				chd_obj_bbox.append(chd_obj_bbox_ymax)
				chd_obj.append(chd_obj_bbox)
				root.append(chd_obj)


				s = etree.tostring(root, pretty_print=True)

				#line = label[file_name] + ' 1 1 ' + str(img.shape[0]) + ' ' + str(img.shape[1]) + '\n'
				print s
				out.write(s)
				#cv2.imshow('image', img)
				#cv2.waitKey(0)
				#raw_input()

if __name__ == "__main__":
	#label = read_label('/home/sui/workspace/cnn_data/progress/trainimage.txt')
	#process_one_folder('/home/sui/workspace/cnn_data/progress/train/', label)

	label = read_label('/home/sui/workspace/cnn_data/progress/testimage.txt')
	process_one_folder('/home/sui/workspace/cnn_data/progress/test/', label)
