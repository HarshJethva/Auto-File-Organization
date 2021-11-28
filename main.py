import os
import os.path
import shutil
import gui

source = gui.source
destination = gui.destination

source += '\\'
destination += '\\'

for i in os.listdir(source):
    split_tup = os.path.splitext(i)  #---> use for spilt the file name and its extension
    extension=split_tup[1]
    extension = extension[1:]    #-->use slicing method for catch file extension

    if extension == '': #-->skip the folder
        continue 
    
    if not(os.path.isdir(destination + extension)):         
        path = os.path.join(destination, extension)
        os.mkdir(path)

    h = source + i
    j = destination + extension + '\\' + i

    if os.path.exists(j):
        print(i,"already exist")
        continue
    
    shutil.move(h,j)