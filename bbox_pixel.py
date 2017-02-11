#this converts output txt file to pixelwise label
import numpy as np
import numpy.matlib
import numpy, scipy.io
from scipy.io import savemat

#----------
#  0 background
#  1 cloud_b_plush_bear
#  2 creativity_chenille_stems
#  3 hanes_tube_socks
#  4 kyjen_squeakin_eggs_plush_puppies
#  5 laugh_out_loud_joke_book
#----------


dict = {}
dict['background']=0;
dict['cloud_b_plush_bear']=1;
dict['creativity_chenille_stems']=2;
dict['hanes_tube_socks']=3;
dict['kyjen_squeakin_eggs_plush_puppies']=4;
dict['laugh_out_loud_joke_book']=5;


column = 480
row = 270
old_name = ""
fp = open("det_result.txt")
for i, line in enumerate(fp):
    #read in each line 
    words = line.split(" ")
    file_name = words[0]
    item = words[1]
    #get xmin, ymin, xmax, ymax as integer
    bbox = words[2:6]
    bbox_float = [float(a) for a in bbox]
    bbox_int = [int(a) for a in bbox_float]
    #some files contain multiple bounding boxes, the current file name == previous file name
    #else create a new empty matrix 
    if file_name!=old_name:
        #img = np.zeros((row, column),dtype=np.uint8)
        img = np.matlib.zeros((row, column),dtype=np.uint8)
        #create a file to record results
        output_file_name = file_name.replace(".jpg",".mat")
        
        print (output_file_name)
    #assign values to corresponding points in image
    item_class=dict[item]

    xmin = bbox_int[0]
    ymin = bbox_int[1]
    xmax = bbox_int[2]
    ymax = bbox_int[3]
    print (xmin)
    print (ymin)
    print (xmax)
    print (ymax)
    #img[1:5,1]=4
    img[ymin:ymax+1,xmin:xmax+1]=item_class
    #np.savetxt("result/"+output_file_name,img)
    name_mat = "result/"+output_file_name
    scipy.io.savemat(name_mat, {'result':img})

    #update old file name 
    old_name = file_name

    #view using matlab:imagesc(result)




