### Script to print list of files and directories

from os import listdir
from os.path import isfile, join
from os import walk

# path to list files in
# mypath = "//pscnas/CustDeliverables/BookScan/CustomGeo/output_files/"
mypath = "V:/BookScan/BookScan 'Offline Reports' Repository/Early View reports/Approved reports/SAS"

########################

# lists only files, not directories
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
print(onlyfiles)

########################

# lists only files, not directories (just another method)
# if you remove the break command it should create two lists, files and directories
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
	f.extend(filenames)
	break
# print(f)

#######################

# lists everythign in path alphabetically
# print(listdir(mypath))