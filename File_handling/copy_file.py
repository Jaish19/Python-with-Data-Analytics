from shutil import copyfile, move
import os

img = "de1.txt"

dest_name = "de1.txt"

dest_folder = "dd"

print (os.path.exist(os.path.join(dest_folder,img) ))

image_path_out = os.path.join(dest_folder,img)  # d\\de.txt

copyfile(img, image_path_out)

# move(img, image_path_out))