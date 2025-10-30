import cv2


# imread is used to resd an image by passing the path of the image as input
img = cv2 .imread ("grey scale bird.jpeg", -1)
#there are 3 parameters to read an image -
#cv2.IMREAD_color (1) =>x Specify to load the image in color 
#cv2.IMREAd_GREYSCALE 0 =X Specify to load the image in greyscale / black & white 
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image with a title 
cv2.imshow("Pacman",img)

#To hold the window until the user presses a key on keyboard 
cv2.waitKey(0)

# delete / close the image widow afte the key pressed 
cv2.destroyAllWindows()