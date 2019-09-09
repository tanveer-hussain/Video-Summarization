# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:49:54 2018

@author: Tanveer
"""

import glob
import cv2
import numpy as np

root_dir = 'Keyframes\\temp\\'
pth = root_dir + "*.png"
tt = glob.glob(pth)
#for i in range(1,len(tt)):
#    query_img = cv2.imread(tt[i])
#    image_name = tt[i].split('\\')
#    for j in range(i+1,len(tt)):
#        compare_img = cv2.imread(tt[j])
#        (score,diff) = compare_ssim(query_img,compare_img,full=True,multichannel=True)
#        #print ("Score = " , score)
#        pathh = 'Keyframes\\v11\\VS11\\',image_name[2]
#        print (pathh)
#        if score > 0.7: #means SSIM 
#            cv2.imwrite(pathh, query_img)

count = 0
for i in range(1,len(tt)):
    query_img = cv2.imread(tt[i])
    image_name = tt[i].split('\\')
   
#    query_histt = cv2.calcHist([query_img],[0],None,[255],[0,256])
    for j in range(i+1,len(tt)):
        compare_img = cv2.imread(tt[j])
#        compare_histt = cv2.calcHist([compare_img],[0],None,[255],[0,256])
        
#        distt = cv2.compareHist(query_histt,compare_histt,0)
#        print (" distance = " , distt)
        difference = np.sum((query_img.astype("float") - compare_img.astype("float")) ** 2)
        difference /= float(query_img.shape[0] * compare_img.shape[1])
        

        
        
        #print ("Score = " , score)
        pathh = root_dir + 'kf\\' + image_name[2] 
#        print (pathh)
        if difference < 3000: 
            print ("Writing Image ", pathh)
            cv2.imwrite(pathh, query_img)
#            print ("Different images",count)
            count = count + 1
        
    