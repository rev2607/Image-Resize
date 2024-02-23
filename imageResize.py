import cv2

src = cv2.imread("audi.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("resized", src)
scale_precent = 50

width = int(src.shape[1]*scale_precent/100)
height = int(src.shape[0]*scale_precent/100)

dsize = (width,height)

output = cv2.resize(src,dsize)
cv2.imwrite('resized.jpg',output)
cv2.waitKey(0)
