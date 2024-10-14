from PIL import Image
import os
import sys
 
if len(sys.argv) < 3:
    print("Usage: img2pdf <output pdf path> <path to directory of images> <<Optional switches: -dn>>")
    exit(1)

by_name = True

if len(sys.argv) == 4:
    match sys.argv[3]:
        case "-d":
            by_name = False
        case "-n":
            by_name = True

pdf_path = os.path.abspath(sys.argv[1])
folder = os.path.abspath(sys.argv[2])
print("In: " + folder)
print("Out: " + pdf_path)

images = []

os.chdir(folder)
files = [file for file in os.listdir(folder)]

if by_name:
    files.sort()
else:
    files.sort(key=os.path.getmtime)

for filename in files:
    try:
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    except:
        pass

images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])