import cv2 as cv
import numpy as np

def treshold_image(img, treshold, high_val = None, low_val = 0 ):

    img_result = np.zeros(img.shape, np.uint8)
    i = 0
    j = 0
    while i < img.shape[0]:
        while j < img.shape[1]:
            if(img[i][j] > treshold):
                img_result[i][j] = low_val
            else:
                img_result[i][j] = img[i][j]
            j+=1
        i+=1

    return img

def get_only_blinks_from_images(images):
    sum_of_diffs = np.zeros(images[0].shape, np.uint8)
    image_size = len(images)
    for image_index in range(image_size - 1):
        diff = cv.absdiff(images[image_index], images[image_index+1])
        diff = treshold_image(diff, 50)
        sum_of_diffs = cv.add(diff, sum_of_diffs)

    print(sum_of_diffs)
    # return treshold_image(sum_of_diffs, 5, 1)
    return sum_of_diffs


def get_max_dist_bright_4_points(image):

    pass


def detect_object_from_background(images):

    only_blink_image = get_only_blinks_from_images(images)

    return only_blink_image, only_blink_image