import numpy
import h5py
import json


def convert(filename):

    with open(filename+".txt") as json_file:
        metadata = json.load(json_file)

    print(metadata)

    data = numpy.loadtxt(filename+".dat", skiprows=metadata["FILE_HEADER_LINES"])

    print(data.shape)

    f = h5py.File(filename+'.h5', 'w')
    f1 = f.create_group("metadata")
    f2 = f.create_group("data")

    for key in metadata.keys():
        print(key, metadata[key])
        if metadata[key] is None:
            f1[key] = ''
        else:
            f1[key] = metadata[key]

    for i in range(data.shape[1]):
        f2["col%02d"%i] = data[:,i]


    f.close()
    print("File written: ", filename+'.h5')

if __name__ == "__main__":
    import os
    os.system("rm -f *.h5")
    convert("dabam-001")



