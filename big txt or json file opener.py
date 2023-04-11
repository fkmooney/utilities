### This can be used to open big json files one line at a time. 
### It can be used to open other big .txt files.

def read_big_file(filename):
    with open(filename, "r") as _file:
        count = 0
        
        for line in _file: 
            if count < 30:
                print(line)
                count = count + 1
            else: 
                break


f = "AMZ-bookscan-weekly-13.json"  # amazon json file name
read_big_file(f) 
