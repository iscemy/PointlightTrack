from read_test_images import *
from initial_obj_detect_cam import *
from matplotlib import pyplot as plt

images = read_test_images("../sim_export/", "cam1_", ".png", 100)

ret_int, ret = detect_object_from_background(images)

print(len(images))

figure, axis = plt.subplots(2, 1)
axis[0].imshow(ret)
axis[1].imshow(ret_int)

plt.show()
