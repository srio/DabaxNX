from silx.io.specfile import SpecFile
import h5py

def convert(filename):

    sf = SpecFile(filename+".dat")

    s1 = sf[0]


    f = h5py.File(filename+'.h5', 'w')
    f["header"] = str(s1.header)

    for index in range(len(sf)):
        s1 = sf[index]
        name = s1.scan_header_dict["S"]
        f1 = f.create_group(name)

        for i,label in enumerate(s1.labels):
            f1[label] = s1.data[i,:]

        f2 = f1.create_group("metadata")
        for key in s1.scan_header_dict.keys():
            f2[key] = s1.scan_header_dict[key]


    f.close()
    print("File written: ", filename+'.h5')

if __name__ == "__main__":
    import os
    os.system("rm -f *.h5")
    convert("AtomicConstants")
    convert("f1f2_EPDL97")
    convert("Crystals")




    from silx.io.convert import convert

    convert("AtomicConstants.dat", "AtomicConstantsCONVERT.h5")
    convert("f1f2_EPDL97.dat", "f1f2_EPDL97CONVERT.h5")
    convert("Crystals.dat", "CrystalsCONVERT.h5")

