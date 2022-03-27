import numpy as np
from numpy import asarray
import cv2;

img= cv2.imread("l.png",0);

cv2.imshow('image',img);


cv2.waitKey(0);

np_img=asarray(img)

print(np_img)


print("rowXcolumn :",img.shape)

print("image size :",np.size(img))

brightness=round((np.sum(img))/(np.size(img)))

print("max pixel value of image :",np.max(img))

print("min pixel value of image :",np.min(img))

contrast=np.max(img)-np.min(img)
cv2.destroyAllWindows()

print("The brightness of the image is = {}\n The contrast of the image is = {}".format(brightness,contrast))