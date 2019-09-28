#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import shutil
import time

RAW = {'.CR2', '.cr2', '.NEF', '.nef', '.DNG', '.dng',}
JPG = {'.JPG', '.jpg',}

def readFileName(f_path):
    if(os.path.exists(f_path)):
        file_names = os.listdir(f_path)
        for file in file_names:
            split_name = os.path.splitext(file)
            if split_name[1] in JPG:
                shutil.move(os.path.join(f_path, file), os.path.join(f_path, 'JPG', file))
                print("Move {} to folder JPG".format(file))
            if split_name[1] in RAW:
                shutil.move(os.path.join(f_path, file), os.path.join(f_path, 'RAW', file))
                print("Move {} to folder RAW".format(file))
            
def generateFolders(f_path):
    if(os.path.exists(f_path)):
        if os.path.exists(os.path.join(f_path, 'JPG')):
            print("JPG EXIT!")
        else:
            os.makedirs(os.path.join(f_path, 'JPG'))
            print("JPG GENERATED")
        if os.path.exists(os.path.join(f_path, 'RAW')):
            print("RAW EXIT!")
        else:
            os.makedirs(os.path.join(f_path, 'RAW'))
            print("RAW GENERATED")
            
current_path = os.getcwd()
start_time = time.time()
generateFolders(current_path)
readFileName(current_path)
end_time = time.time()
print("Used time: {} s".format(end_time-start_time))
