import pydicom
import matplotlib.pyplot as plt
import numpy as np
import os
import multiprocessing
import time

def saveAsJPGImage(img_array, jpg_path, uid, lens):
    """
	Format conversion function
	input :  Pixel matrix,Picture save path,uid,lens
	output: 
	"""
    plt.figure(figsize=(12,6),dpi=80)                 # draw drawing board
    arr_temp  = np.reshape(img_array,(lens,))
    max_val   = max(arr_temp)                         # Get pixel maximum value
    min_val   = min(arr_temp)                         # Get pixel minimum value
    img_array = (img_array-min_val)/(max_val-min_val) # pixel value normalization
    plt.imshow  (img_array,cmap=plt.cm.bone)
    plt.title   ("UID:{}".format(uid))
    plt.savefig (jpg_path)
    plt.close   ()

def getDicomFile(dicom_dir, jpg_dir):
    """
    Get parameter information of dicom file
    input : dicom_dir,jpg_dir
    output: args_list
    """
    # Position absolute path
    all_file_list = os.listdir(dicom_dir)

    # Initialize args_list
    args_list     = []

    for f in all_file_list:
        dicom_file_path = os.path.join(dicom_dir, f)
        dcm             = pydicom.read_file(dicom_file_path)      # read dicom file
        img_array       = dcm.pixel_array                         # Get image pixel matrix
        orientation     = dcm.ImageOrientationPatient

        if orientation ==   ['1', '0', '0', '0', '0', '-1']:
            jpg_name        = jpg_dir + "/cor/" + f.split('.d')[0] + '.jpg'     # Coronal View

        elif orientation == ['0', '1', '0', '0', '0', '-1']:
            jpg_name        = jpg_dir + "/sag/" + f.split('.d')[0] + '.jpg'     # Sagital View
        
        else:
            jpg_name        = jpg_dir + "/ax/" + f.split('.d')[0] + '.jpg'      # Axial View


        lens            = img_array.shape[0] * img_array.shape[1]    # Get pixel matrix size
        uid             = dcm.SOPInstanceUID                         # Get image uid
        args_tuple      = (img_array, jpg_name, uid, lens)           # Add parameter tuple
        args_list.append(args_tuple)
    return args_list


def main():
    """
    main function
    """
    # Folder of DICOM files
    dicom_dir  = "data/dicom/"
    # Folder to store JPG pictures
    jpg_dir    = "data/jpg"
    begin_time = time.time()                       # Starting time
    pool       = multiprocessing.Pool(processes=5) # Create process pool
    args_list  = getDicomFile(dicom_dir,jpg_dir)   # Get parameter list
    pool.starmap(saveAsJPGImage, args_list)        # Save jpg files in multiple processes
    pool.close()                                   # Close the process
    end_time   = time.time()                       # End Time
    print("Time-consuming: {}s".format(round(end_time-begin_time,4))) # Printing time-consuming


if __name__ == '__main__':
	main()