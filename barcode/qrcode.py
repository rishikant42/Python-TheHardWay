from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print('Type: ', obj.type)
    print('Data: ', obj.data)

  return decodedObjects

im = cv2.imread('test2.png')

decodedObjects = decode(im)
