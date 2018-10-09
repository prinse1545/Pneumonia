#Philipp Moura Srivastava
#October 8 2018
#pneumoniaClassifier.py
#
#This file classifies stuff
import os
from os import listdir
import pydicom
from pydicom.data import get_testdata_files
import cv2
from pathlib import Path



def main():
    #Getting image names in a list
    imageNames = os.listdir('./stage_1_test_images')


    for name in imageNames:
        #Converting images to PNG JPG
        convertToImage(name)




def convertToImage(imageName):
    # A function
    path = "./stage_1_test_images/" + imageName
    path_to_folder = "./stage_1_test_images/"
    jpg_folder_path = "./images"
    #checking if file exists

    checkFile = Path(path)

    if(checkFile.is_file()):
        ds = pydicom.dcmread(path)
        imageName = imageName.replace('.dcm', '.png')
        print(imageName)
        cv2.imwrite(jpg_folder_path + imageName, ds)
    else:
        print("ERROR: FILE NOT FOUND! Make sure the folder stage_1_test_images is in the root folder")


    #writing image as PN



main()
