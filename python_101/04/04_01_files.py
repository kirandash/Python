# Files

def main():
    # open a file for writing and creating it if doesn't exist
    f = open("python_101/04/textfile.txt", "w+")

    # write some lines of data to the file
    for i in range(15): # 15 not included
        f.write("This is line " + str(i) + "\r\n")

    # close file when done
    f.close()

    # open the file for appending text to the end
    fa = open("python_101/04/textfile.txt", "a")

    # write some lines of data to the file
    for i in range(15, 20):
        fa.write("This is line " + str(i) + "\r\n")

    # open the file back up & read it's contents
    fr = open("python_101/04/textfile.txt", "r")

    if fr.mode == 'r': # to make sure file was successfully open before reading it
        contents = fr.read()
        print(contents)

    # reading line by line intead of entire content. Thus can limit how many lines to read instead of reading it all
    fr_line = open("python_101/04/textfile.txt", "r")

    if fr_line.mode == 'r':
        fl = fr_line.readlines()
        for x in fl:
            print(x)

if(__name__ == "__main__"):
    main()