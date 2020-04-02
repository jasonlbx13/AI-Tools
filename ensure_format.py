from PIL import Image
from tqdm import tqdm
import os

def format_ensure(img_dir):
    img = Image.open(img_dir)
    form = img.format
    if (form != 'JPEG') and (form != 'JPG'):
        img.save(img_dir[0:-3]+form)
        os.remove(img_dir)
    else:
        pass
    return form

def clean_format(img_file):
    img_list = os.listdir(img_file)
    for i in tqdm(range(len(img_list))):
        try:
            img_name = img_list[i]
            img_format = format_ensure(img_file+'/'+img_name)

#             if img_format == 'PNG':
#                 print (img_name+' has been turn to .PNG')
#             else:
#                 pass

        except:
            print (img_file+'/'+img_name+' file is error!')

    print (img_file+' is done')
    return None

if __name__ == '__main__':

    database_dir = './data/politician'
    database_list = os.listdir(database_dir)

    for img_file in database_list:

        try:
            clean_format(database_dir+'/'+img_file)

        except:
            print (img_file+' has something wrong')
            continue