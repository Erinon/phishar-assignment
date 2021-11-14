import os
from pathlib import Path
import numpy as np
import cv2 as cv


def read_non_empty_lines(path):
    with open(path, "r") as f:
        lines = f.read().splitlines()

        return list(filter(lambda l: not l.startswith("#"), lines))

def read_img_grayscale(path):
    return cv.imread(path, cv.IMREAD_GRAYSCALE)

def read_img_from_bytes_grayscale(img_bytes):
    bts = np.frombuffer(img_bytes, np.uint8)
    return cv.imdecode(bts, cv.IMREAD_GRAYSCALE)

def list_average(lst):
    if len(lst) == 0:
        return float("inf")

    return sum(lst) / len(lst)
