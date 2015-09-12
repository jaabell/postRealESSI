import h5py
import scipy as sp
import domain_components
from RealESSIModel import RealESSIModel



def open_essi_output_file(filename):
    if h5py.is_hdf5(filename): #Check if the file is valid
        return RealESSIModel(filename)
    else:
        print "The file ", fileNameIn, " is not a valid HDF5 file."

