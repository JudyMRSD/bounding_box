import re
import os
import xml.etree.ElementTree as ET
import pdb;

#rootdir = '/home/akshaybhagat/Downloads/collection (1)/Annotations/users/JudyMRSD/50_items_5_classes_tighterpolygon/'
rootdir = '/Users/jinzhu/Google\ Drive/2017\ spring/APC/faster\ rcnn/data'
data_set_folder="polygon_xml"
annotation_dir="/Users/jinzhu/Google\ Drive/2017\ spring/APC/faster\ rcnn/data/bbox_xml"

#n number of tabs indent
def ntabs(n):
	string=""
	for _ in range(n):
		string=string+"\t"
	return string

def tag_and_contents(tag,contents,leaf=0):
	spacing="\n"
	if leaf: spacing=""
	string="<"+tag+">"+spacing+str(contents)+"</"+tag+">\n" 
	return string

def poly_to_bb(filepath):
	named_box=[]
	bbox=[]

	file=""
	for i,line in enumerate(open(filepath)):
		file=file+line
	
	item_names = re.findall("<name>[\s\S]*?<\/name>", file, re.DOTALL)
	item_names=[re.sub('<.*?>', '', match) for match in item_names]
	polygons=re.findall("<polygon>[\s\S]*?<\/polygon>", file, re.DOTALL)
	for polygon in polygons:
		x_cords=re.findall("<x>[\s\S]*?<\/x>",polygon,re.DOTALL)
		x_cords=[int(re.sub('<.*?>','',x)) for x in x_cords] 
		x_cords.sort()
		y_cords=re.findall("<y>[\s\S]*?<\/y>",polygon,re.DOTALL)
		y_cords=[int(re.sub('<.*?>','',y)) for y in y_cords] 
		y_cords.sort()
		bbox.append([(x_cords[0],y_cords[0]),(x_cords[-1],y_cords[-1])])
		named_box=zip(item_names,bbox)	

	return named_box
	
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		filepath= os.path.join(subdir, file)
		#import pdb;pdb.set_trace()
		named_box=poly_to_bb(filepath)
		
		#writing to the new file 
		tree=ET.parse(filepath)
		root=tree.getroot()
		outfile=open(annotation_dir+file,"w+")
		content=""
		content=content+tag_and_contents("folder",data_set_folder,1)
		content=content+tag_and_contents("filename",root.find("filename").text,1)
		content=content+tag_and_contents("size",tag_and_contents("width",root.find('imagesize').find('ncols').text,1)+tag_and_contents("height",root.find("imagesize").find("nrows").text,1)
			+tag_and_contents("depth","3"))
		content=content+tag_and_contents("segmented",0,1)
		for i in named_box:
			content=content+tag_and_contents("object",tag_and_contents("name",i[0])+tag_and_contents("pose","Unspecified")+tag_and_contents("truncated",0)+tag_and_contents("bndbox",tag_and_contents("xmin",i[1][0][0],1)+tag_and_contents("ymin",i[1][0][1],1)
				+tag_and_contents("xmax",i[1][1][0],1)+tag_and_contents("ymax",i[1][1][1],1)))
		#ending of xml file
		content=tag_and_contents("annotation",content)
		outfile.write(content)
		print(annotation_dir+file)
		outfile.close
