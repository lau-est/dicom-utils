import os

from numpy.lib.function_base import angle
import pydicom as dicom

"""
Reading a single image
"""

# Set the local dicom file
folder_path = "data"
file_name   = "IM-0001-0001.dcm"
file_path   = os.path.join(folder_path, file_name)
ds          = dicom.dcmread(file_path)



"""
Reading a dicom with missing file meta-information
    If the following errors may occur:
    (1) raise InvalidDicomError("File is missing DICOM File Meta Information
    (2) pydicom.errors.InvalidDicomError: File is missing DICOM File Meta Information header or the 'DICM' prefix is missing from the header. Use force=True to force reading.
"""
#ds                             = dicom.dcmread(file_path, force = True)
#ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian


"""
Reading and editing dicom tags
"""
# First way: description of the used tag
print("Patient ID: ", ds.PatientID, " Study Date: ", ds.StudyDate, " Modality: ", ds.Modality)

# Second tag: ds.get() function
patient_id = ds.get(0x00100020)
print(patient_id)


"""
Processing: After reading you can use Numpy and image processing lybraries
"""
# Using Numpy
import numpy as np
data = np.array(ds.pixel_array)
print(data.shape)

# Using PIL image
from PIL import Image
data_img         = Image.fromarray(ds.pixel_array)
data_img_rotated = data_img.rotate(angle=45, resample=Image.BICUBIC, fillcolor=data_img.getpixel((0, 0)))

# Show above is rotation. There are other functions such as resize as well :D
# NOTE: It should be noted that sometimes when converting numpy's ndarray to Image, it generally changes
print(data.dtype)                           #int16
data_rotated = np.array(data_img_rotated)
print(data_rotated.dtype)                   #int32

# Just specify the parameter to solve it
#data_rotated = np.array(data_img_rotated, dtype = np.int16)



"""
Visualization
"""

# Using Matplotlib
# Note cmap bone cannot meet the whole requirements of medical images
from matplotlib import pyplot
pyplot.imshow(ds.pixel_array, cmap=pyplot.cm.bone)
pyplot.show()

# Using PIL
# Click on the image to see the commands window
data_img.show()

"""
Single image writing
"""
ds.PixelData        = data_rotated.tobytes()
ds.Rows, ds.Columns = data_rotated.shape
new_name            = "dicom_rotated.dcm"
ds.save_as(os.path.join(folder_path, new_name))