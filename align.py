import face_recognition
import cv2
from PIL import Image
import os
import argparse



def main(args):

    img_name_book = os.listdir(args.input_dir)
    try:
        img_name_book.sort(key=lambda x: int(x[:-4]))
    except:
        pass

    for img_name in img_name_book:
        image = face_recognition.load_image_file(args.input_dir+'/'+img_name)
        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
        face_num = len(face_locations)
        for i in range(face_num):
            top, right, bottom, left = face_locations[i]
            pad = 0.25
            new_top = int(top - (bottom - top) * pad) if int(top - (bottom - top) * pad) > 0 else top
            new_bottom = int(bottom + (bottom - top) * pad) if int(bottom + (bottom - top) * pad) < len(image) else bottom
            new_left = int(left - (right - left) * pad) if int(left - (right - left) * pad) > 0 else left
            new_right = int(right + (right - left) * pad) if int(right + (right - left) * pad) < len(image[0]) else right
            face_image = image[new_top:new_bottom, new_left:new_right]
            face_image = Image.fromarray(face_image)
            face_image.save('{}/{}_{}.jpg'.format(args.output_dir, img_name[:-4], i))
    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='align facr from pictures')
    parser.add_argument('--input_dir', help='images file direction')
    parser.add_argument('--output_dir', help='face save direction')
    args = parser.parse_args()

    main(args)
    print ('done')
