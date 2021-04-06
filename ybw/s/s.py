import os
# from cv2 import cv2


def mkdir(name):
    if os.path.exists(name):
        return
    else:
        os.mkdir(name)


def mkdirs(name):
    if os.path.exists(name):
        return
    else:
        os.makedirs(name)


# def im_show(img, name='temp'):
    # cv2.imshow(name, img)
    # cv2.waitKey(0)


j = os.path.join
