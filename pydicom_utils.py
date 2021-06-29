import pydicom 
import os
import matplotlib.pyplot as plt
import numpy as np

"""
Read a dicom file
# Get the meta data information of the image through
# dictionary keywords. It can also be based on the TAG number.
# Get several common information here
"""
info = {}
dcm  = pydicom.read_file("data/IM-0001-0001.dcm")

info["PatientID"]        = dcm.PatientID         # Patient ID
info["PatientName"]      = dcm.PatientName       # Patient name
info["PatientAge"]       = dcm.PatientAge        # Patient age
info['PatientSex']       = dcm.PatientSex        # Patient gender
info['StudyID']          = dcm.StudyID           # Check ID
info['StudyDate']        = dcm.StudyDate         # Check date
info['StudyTime']        = dcm.StudyTime         # check the time
info['InstitutionName']  = dcm.InstitutionName   # institution name
info['Manufacturer']     = dcm.Manufacturer      # equipment manufactory
info['StudyDescription'] =dcm.StudyDescription   # Check item description
#print(info)

"""
Get the pixel matrix in the image Tag and save it as JPG or PNG
# It uses matplotlib lybrary for drawing and numpy for matrix 
# operation.
"""
file_name = "data/IM-0001-0012.dcm"
png_name  = "data/test.png"

# Read dicom file
dcm_1 = pydicom.read_file(file_name)

# Get image unique identifier UID
uid = dcm.SOPInstanceUID

# Get pixel matrix
img_arr = dcm.pixel_array

# Print matrix size
print(img_arr.shape)

# Get the number of pixels
lens = img_arr.shape[0] * img_arr.shape[1]

# Get the maximum and minimum values of pixels
arr_temp = np.reshape(img_arr, (lens, ))
max_val  = max(arr_temp)
min_val  = min(arr_temp)

# Image normalization
img_arr = (img_arr - min_val)/(max_val - min_val)

# Draw the image and save
# Image can be set according to different files
plt.figure(figsize=(12,12), dpi = 250) 
plt.imshow(img_arr, cmap=plt.cm.bone)
plt.title ("UID:{}".format(uid))
plt.savefig(png_name)
plt.show()
plt.close()


