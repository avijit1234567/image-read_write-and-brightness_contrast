# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:45:40 2022

@author: USER
"""

import cv2
 
img = cv2.imread("l.png",0)
 
cv2.imshow("hello", img)
 
cv2.waitKey(0)

 
cv2.destroyAllWindows()