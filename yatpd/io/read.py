# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np


def imread(file_path):
    '''Read a single image from a file.

    Parameters
    ----------
    file_path: str
      Path of file.
    '''
    return cv2.imread(file_path)


def flread(folder_path):
    '''Read images from a folder.

    Parameters
    ----------
    folder_path: str
      Path of folder.
    '''
    img_type = ['bmp', 'dib', 'jpeg', 'jpg', 'jpe',
                'png', 'pbm', 'pgm', 'ppm', 'sr',
                'ras', 'tiff', 'tif', 'exr', 'jp2']
    file_name_list = os.listdir(folder_path)
    img_list = []
    for file_name in file_name_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.splitext(file_path)[1][1:].lower() not in img_type:
            continue
        img_list.append(imread(file_path))
    return img_list
