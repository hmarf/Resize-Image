from PIL import Image
import os

def resizeImageWithConvert(input_file, output_file):

    imagePil = Image.open(input_file)
    w,h = imagePil.size
    size = 640

    if w > h:
        _w = 640
        _h = h / w * size
    elif w < h:
        _h = 640
        _w = w / h * size
    else:
        _w = 640
        _h = 640

    img = imagePil.resize((int(_w),int(_h)),resample=Image.BICUBIC)
    img.save(output_file, quality=85)

if __name__ == '__main__':
    
    input_dir = ''
    output_dir = ''
    dirs = os.listdir(input_dir)
    for _dir in dirs:
        input_file = input_dir+_dir
        output_file = output_dir+_dir
        resizeImageWithConvert(input_file,output_file)