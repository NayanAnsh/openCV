import cv2 as cv 
image =  cv.imread("C:\\Users\\Nayan\\Downloads\\duck.jpg")
cv.imshow("IMAGE" , image)
print(image)
key = cv.waitKey(0) # returns unicode of pressed key
if key == ord("s"):
    cv.imwrite("image.png",image)
    print("Image saved")
    
    