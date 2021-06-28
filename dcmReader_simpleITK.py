import SimpleITK as sitk
import os

"""
Reading a single image
"""

# Set the local dicom file
folder_path = "data"
file_name   = "IM-0001-0001.dcm"
file_path   = os.path.join(folder_path, file_name)

"""
sitk.ReadImage()
    This method directly returns the image object, which is simple and easy to understand.
    However, the value of Tag cannot be read
"""

img = sitk.ReadImage(file_path)
print(type(img))                # <class 'SimpleITK.SimpleITK.Image'>


"""
sitk.ImageFileReader()
    This method is more like C++ operation style, you need to initialize an object first.
    Then, set some parameters, and finally return to image. It is relatively more complicated, 
    but trhere are more points that can be manipulated
"""
file_reader = sitk.ImageFileReader()
file_reader.SetFileName(file_path)
data = file_reader.Execute()
# Reading the dicom tag
#for key in file_reader.GetMetaDataKeys():
    #print(key, file_reader.GetMetaData(key)) 


# The above two methods return three-dimensional objects, which is very different from Pydicom
data_np = sitk.GetArrayFromImage(data)
print(data_np.shape)                  ## (1, 512, 512) = (Slice index, Rows, Columns)


"""
Sequence Read
"""
series_reader = sitk.ImageSeriesReader()
file_names    = series_reader.GetGDCMSeriesFileNames(folder_path)
series_reader.SetFileNames(file_names)
images = series_reader.Execute()
data_all = sitk.GetArrayFromImage(images)
print(data_all.shape)


"""
Some Operations: Edge detection
"""
# 1) sitk.CannyEdgeDetection()
# Since the filtered object must be a 32-bit image or other format, it needs to pass
# sitk.Cast() Conversion. You can then convert back to the original format.

data_32     = sitk.Cast(data, sitk.sitkFloat32)
data_edge_1 = sitk.CannyEdgeDetection(data_32, 5, 30, [5]*3, [0.8]*3)

# 2) sitk.CannyEdgeDetectionImageFilter()
# This operation is relatively troublesome

Canny = sitk.CannyEdgeDetectionImageFilter()
Canny.SetLowerThreshold(5)
Canny.SetUpperThreshold(30)
Canny.SetVariance([5]*3)
Canny.SetMaximumError([0.5]*3)
data_edge_2 = Canny.Execute(data_32)

"""
Visualization
"""
import sys
sitk.Show(data_edge_1, 'sample image', debugOn=True)
