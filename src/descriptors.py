import os
import cv2 as cv

import constants as con
import util


def get_detector(name):
    if name == "ORB":
        return cv.ORB_create(nfeatures=con.DETECTOR_FEATURES)

    raise Exception("Invalid detector.")

def get_matcher(name):
    if name == "BF":
        return cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

    raise Exception("Invalid matcher.")

def get_image_descriptors(detector, img):
    _, descriptors = detector.detectAndCompute(img, None)
    return descriptors

def get_host_descriptors(detector, hosts):
    descriptors = {}

    for host in hosts:
        img_path = os.path.join(con.IMAGES_PATH, host + ".png")
        img = util.read_img_grayscale(img_path)

        descriptors[host] = get_image_descriptors(detector, img)

    return descriptors

def get_distance(matcher, desc1, desc2):
    distances = matcher.match(desc1, desc2)
    distances = list(map(lambda x: x.distance, distances))
    distances = sorted(distances)[:con.RELEVANT_FEATURES]

    return util.list_average(distances)

def get_best_match(matcher, descriptors, known_desctiptors):
    best_host = ""
    best_distance = float("inf")

    for host, host_descriptors in known_desctiptors.items():
        distance = get_distance(matcher, descriptors, host_descriptors)

        if distance < best_distance:
            best_host = host
            best_distance = distance

    return best_host, best_distance
