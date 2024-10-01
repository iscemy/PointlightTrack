import cv2 as cv

def read_test_images(folder_path, prefix, suffix, num_of_images, offset = 1):
    imgArray = []
    for index in range(num_of_images):
        filePath = folder_path + prefix + str(index + offset) + suffix
        im = cv.imread(filePath, cv.IMREAD_GRAYSCALE)
        imgArray.append(im)

    return imgArray