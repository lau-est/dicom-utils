# DICOM Reading

Simple functions to read a dicom using Numpy, PIL and SimpleITK


## Prerequisites


It is recommended the use of Anaconda.
If you are using Anaconda, you can use the next commands:

```
conda install -c conda-forge pydicom
conda install -c anaconda numpy
conda install -c anaconda pillow
conda install -c conda-forge matplotlib
conda install -c simpleitk simpleitk
conda install -c simpleitk/label/dev simpleitk
conda install -c bioconda fiji

```

## To execute using Numpy and PIL
```
python dcmReader_numpyPIL.py

```

## To execute using Numpy and SimpleITK
```
python dcmReader_simpleITK.py

```

## To execute pydicom utils for reading a single Dicom
```
python pydicom_utils.py

```

## To execute pydicom utils for reading multiple Dicom files and for converting to JPG images
```
python pydicom_utils_multiple_files.py

```
