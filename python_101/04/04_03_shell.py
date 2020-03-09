# Filesystem Shell methods
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # create a duplicate file
    if (path.exists("python_101/04/textfile.txt")):
        # get path to the file in current directory
        src = path.realpath("python_101/04/textfile.txt")

        # make a backup copy by appending .bak to the name
        dst = src + ".bak"

        # copy over the permissions, modification times, and other info
        shutil.copy(src, dst) # copies only content but with new metadata
        shutil.copystat(src, dst) # copies with meta data same as original

        # rename the original file
        if(path.exists("python_101/04/rename.txt")):
            os.rename("python_101/04/rename.txt", "python_101/04/textfile_renamed.txt")

        # create zip archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip: # creates a new zipFile testzip, with keyword helps us create an object and instantiate it as newzip
            newzip.write("python_101/04/textfile.txt")
            newzip.write("python_101/04/textfile.txt.bak")


if __name__ == "__main__":
    main()