import os
folder_path = 'C:\\Users\\a\\PycharmProjects\\pythonProject6\\music'                      # Set the folder path where your files are located

for f in os.listdir(folder_path):
    file_path = os.path.join(folder_path, f)
    if os.path.isfile(file_path):
        filename,filesuffix=os.path.splitext(f)                                           #devide into two parts  base name and extension
        listfile=filename.split(' ')                                                      #making list
        listfile = [item.replace("(", "").replace(")", "") for item in listfile]          #to delete the ( and  )
        listfile = [item for item in listfile if item != '-' and not item.isnumeric()]    #delete '_' char
        new_filename = "".join(listfile) + filesuffix
        new_file_path = os.path.join(folder_path, new_filename)                           # Join the list of words back into a single string
        os.rename(file_path, new_file_path)





