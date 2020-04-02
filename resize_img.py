import cv2
import os
import argparse



def main(args):
    img_name_book = os.listdir(args.input_dir)
    try:
        img_name_book.sort(key=lambda x: int(x[:-4]))
    except:
        pass
    for img_name in img_name_book:
        img = cv2.imread(args.input_dir+'/'+img_name)
        img = cv2.resize(img,(int(args.img_weight), int(args.img_height)))
        cv2.imwrite(args.input_dir+'/'+img_name, img)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='resize pictures')
    parser.add_argument('--input_dir', help='image direction')
    parser.add_argument('--img_height', default=512, help='image height')
    parser.add_argument('--img_weight', default=512, help='image weight')
    args = parser.parse_args()

    main(args)
    print ('done')
