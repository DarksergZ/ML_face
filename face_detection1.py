#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:37:55 2018

@author: user
"""

import time

import sys

import dlib



start_time = time.clock()    

detector = dlib.get_frontal_face_detector()
window = dlib.image_window()

for face in sys.argv[1:]:
    print("Processing file: {}".format(face))
    img = dlib.load_rgb_image(face)
 
    detection = detector(img, 1)
    print("Count of faces detected: {}".format(len(detection)))
    for i, det in enumerate(detection):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, det.left(), det.top(), det.right(), det.bottom()))

    window.clear_overlay()
    window.set_image(img)
    window.add_overlay(detection)
    dlib.hit_enter_to_continue()



if (len(sys.argv[1:]) > 0):
    img = dlib.load_rgb_image(sys.argv[1])
    detection, scores, idx = detector.run(img, 1, -1)
    for i, det in enumerate(detection):
        print("Detection {}, score: {}, face_type:{}".format(
            det, scores[i], idx[i]))
                                                                                                                        
print (time.clock() - start_time)