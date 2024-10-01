import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def treshold_image(img, treshold_factor):
    i = 0
    j = 0

    imgred = cv.extractChannel(img, 2)
    imggreen = cv.extractChannel(img, 1)
    imgblue = cv.extractChannel(img, 0)

    mean_red = cv.mean(imgred)[0]
    mean_green = cv.mean(imggreen)[0]
    mean_blue = cv.mean(imgblue)[0]

    mean_all = mean_red + mean_green + mean_red

    mean_all = mean_all / 3

    max_r = cv.minMaxLoc(imgred)[1]
    max_g = cv.minMaxLoc(imggreen)[1]
    max_b = cv.minMaxLoc(imgblue)[1]

    max_channel_avg = max_r + max_g + max_b
    max_channel_avg = max_channel_avg / 3

    treshold_red = mean_red * treshold_factor
    treshold_green = mean_green * treshold_factor
    treshold_blue = mean_blue * treshold_factor

    img_ret = img
    while i < img.shape[0]:
        while j < img.shape[1]:
            sum_of_all_channels = imgred[i][j] + imggreen[i][j] + imgblue[i][j]
            if(imgred[i][j] < treshold_red):
                imgred[i][j] = 0
            if(imggreen[i][j] < treshold_green):
                imggreen[i][j] = 0
            if(imgblue[i][j] < treshold_blue):
                imgblue[i][j] = 0

            if(sum_of_all_channels > max_channel_avg):
                imgred[i][j] = 0
                imggreen[i][j] = 0
                imgblue[i][j] = 0


            j+=1
        i += 1

    img_ret = cv.merge([imgblue, imggreen, imgred])

    return img_ret

img = cv.imread("test_images/cam1_17.png")

img_blurred = cv.GaussianBlur(img, (5,5), 1)

figure, axis = plt.subplots(2, 1)
axis[0].imshow(img)
axis[1].imshow(img_blurred)

img_blurred_treshold = treshold_image(img_blurred, 0.7)

figure, axis = plt.subplots(2, 1)
axis[0].imshow(img_blurred)
axis[0].imshow(img_blurred_treshold)

img_blurred_treshold = cv.Canny(img_blurred_treshold, 100, 100)

detector = cv.SIFT_create()
keypoints = detector.detect(img_blurred_treshold, None)
img_blurred_treshold_keypoints = cv.drawKeypoints(img_blurred_treshold, keypoints, np.array([]), (0,255,0), cv.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

print(len(keypoints))

figure, axis = plt.subplots(2, 1)
axis[0].imshow(img_blurred_treshold)
axis[1].imshow(img_blurred_treshold_keypoints)


plt.show()