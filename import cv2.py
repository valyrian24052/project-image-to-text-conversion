import cv2 as cv
import pandas as pd
from statistics import mean
from matplotlib import pyplot as plt


e='cv.TM_CCORR_NORMED'

method = eval(e)


si=cv.imread('./images/result_Page_2.jpg',0)
hi=cv.imread('./symbols/7.png',0)
img=si.copy()
# print(hi.shape)
w, h = hi.shape[::-1]
# print(si.shape, hi.shape)



print(type(si))
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)

# print(max_val)
cr1=img[350:550,150:365]
cr2=img[350:550,365:580]
cr3=img[350:550,580:795]
cr4=img[350:550,795:1010]
plt.imshow(cr2)
plt.imshow(hi)


res = cv.matchTemplate(cr1, hi, method)
print(cv.minMaxLoc(res)[1])
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# print(res.shape)

# cv.rectangle(img,top_left, bottom_right, (255, 0, 0), 2)
# plt.subplot(121),plt.imshow(res,cmap = 'gray')
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img,cmap = 'gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.show()

# x,y =res.shape

# m=0
# for a in range(x):
#     m+=res[a].mean()

# print(m)


