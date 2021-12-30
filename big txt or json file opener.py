### This can be used to open big json files one line at a time. 
### It can be used to open other big .txt files.

def read_big_file(filename):
    with open(filename, "r") as _file:
         for line in _file:
             print(line)

f = "C:/Users/Kempton Mooney/Desktop/bookscan_weekly.json"  # amazon json file name


read_big_file(f) 
