import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import cv2
'''

binimage = imread('1_1.jpg')
plt.imshow(binimage)
bbox=np.zeros(4)
bbox[0]=129
bbox[1]=131
bbox[2]=176
bbox[3]=196 
plt.Rectangle((bbox[0], bbox[1]),
		bbox[2] - bbox[0],
		bbox[3] - bbox[1], fill=False,
		edgecolor='red', linewidth=3.5)

'''
im = cv2.imread('1_1.jpg')
bbox=np.zeros(4)
bbox[0]=247
bbox[1]=135
bbox[2]=313
bbox[3]=190 
#left top, righ bottom
cv2.rectangle(im, (int(bbox[0]), int(bbox[3])), (int(bbox[2]), int(bbox[1])), (255,0,0), 2)
cv2.imshow("ground truth", im)
cv2.imwrite("output.jpg", im)
